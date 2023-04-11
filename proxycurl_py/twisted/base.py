from twisted.internet import defer, reactor
from twisted.internet.defer import Deferred, inlineCallbacks
from proxycurl_py.config import MAX_WORKERS
import treq
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
    List,
    Tuple,
    Callable,
    Dict
)
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')
Op = Tuple[Callable, Dict]


@dataclass
class Result(Generic[T]):
    success: bool
    value: T
    error: BaseException


class ProxycurlException(Exception):
    """Raised when InternalServerError or network error or request error"""
    pass


class ProxycurlBase:
    api_key: str
    base_url: str
    timeout: int
    max_retries: int
    max_backoff_seconds: int

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int,
        max_retries: int,
        max_backoff_seconds: int
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_backoff_seconds = max_backoff_seconds

    @inlineCallbacks
    def request(
        self,
        method: str,
        url: str,
        result_class: Generic[T],
        params: dict = dict(),
        data: dict = dict()
    ) -> Deferred:
        backoff_in_seconds = 1
        for i in range(0, self.max_retries):
            try:
                r = yield self._call(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                )
                if r.code in [200, 202]:
                    response_json = yield r.json()
                    try:
                        defer.returnValue(result_class(**response_json))
                        break
                    except Exception:
                        defer.returnValue(response_json)
                        break
                else:
                    error = yield r.text()
                    raise ProxycurlException(error)
            except ProxycurlException as e:
                if r.code in [400, 401, 403, 404]:
                    logger.exception(str(e))
                    raise e

                if r.code == 500:
                    if i < 1:
                        continue
                    else:
                        raise e

                if r.code == 429:
                    sleep = (backoff_in_seconds * 2 ** i)
                    yield self._sleep(min(self.max_backoff_seconds, sleep))

                if i < self.max_retries:
                    continue
                else:
                    raise e
            except Exception as e:
                logger.exception(str(e))
                if i < self.max_retries:
                    continue
                else:
                    raise e

    def _call(
        self,
        method: str,
        url: str,
        params: dict = dict(),
        data: dict = dict()
    ) -> Deferred:
        api_endpoint = f'{self.base_url}{url}'
        header_dic = {'Authorization': 'Bearer ' + self.api_key}
        if method.lower() == 'get':
            return treq.get(
                api_endpoint,
                params=params,
                headers=header_dic,
                timeout=self.timeout)
        elif method.lower() == 'post':
            return treq.post(
                api_endpoint,
                params=params,
                json=data,
                headers=header_dic,
                timeout=self.timeout)

    def _sleep(secs):
        d = defer.Deferred()
        reactor.callLater(secs, d.callback, None)
        return d


@inlineCallbacks
def do_bulk(ops: List[Op], max_workers: int = MAX_WORKERS) -> List[Result]:
    """Bulk operation

    This function can be used to run bulk operations using a limited number of concurrent requests.

    :param ops: List of operation function and parameter
    :type ops: List[Tuple[Callable, Dict]]
    :param max_workers: Total concurrent request, defaults to 10
    :type max_workers: int
    :return: Once all operation is finished this function will return List[:class:`proxycurl.twisted.base.Result`]
    :rtype: List[:class:`proxycurl.twisted.base.Result`]

    """

    results = [None for _ in range(len(ops))]

    workers = []
    queue = defer.DeferredQueue()

    for job in enumerate(ops):
        queue.put(job)

    for _ in range(max_workers):
        # need to define empty job to stop the worker
        queue.put(None)
        workers.append(_worker(queue, results))

    yield defer.DeferredList(workers)

    defer.returnValue(results)


@inlineCallbacks
def _worker(queue, results):
    while True:
        job = yield queue.get()
        if job is None:
            break

        index, op = job
        try:
            response = yield op[0](**op[1])
            results[index] = Result(True, response, None)
        except Exception as e:
            results[index] = Result(False, None, e)
