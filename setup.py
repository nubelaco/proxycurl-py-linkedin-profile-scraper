# -*- coding: utf-8 -*-
from setuptools import setup

with open ("README.md", "r") as fh:
    long_description = fh.read()

packages = \
['proxycurl_py',
 'proxycurl_py.asyncio',
 'proxycurl_py.gevent',
 'proxycurl_py.twisted']

package_data = \
{'': ['*']}

extras_require = \
{'asyncio': ['asyncio>=3.4.3,<4.0.0', 'aiohttp>=3.7.4,<4.0.0'],
 'gevent': ['gevent>=21.1.1,<22.0.0', 'requests>=2.25.0,<3.0.0'],
 'twisted': ['Twisted>=21.7.0,<22.0.0', 'treq>=21.5.0,<22.0.0']}

setup_kwargs = {
    'name': 'proxycurl-py',
    'version': '0.0.18',
    'description': '',
    'long_description_content_type':"text/markdown",
    'long_description': long_description,
    'author': 'Nubela',
    'author_email': 'tech@nubela.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'package_dir': {'': '.'},
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)