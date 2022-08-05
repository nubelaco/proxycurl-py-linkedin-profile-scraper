# Proxycurl

## What is it?
**Proxycurl** is a set of tools designed to serve as plumbing for fresh and processed data in your application. We sit as a fully-managed layer between your application and raw data so that you can focus on building the application instead of worrying about scraping and processing data at scale.

### With Proxycurl, you can
 - Lookup people
 - Lookup companies
 - Enrich people profiles
 - Enrich company profiles
 - Lookup contact information on people and companies
 - Check if an email address is of a disposable nature

Visit [Proxycurl Official Web](https://nubela.co/proxycurl) for more details.

## Usage
```sh
# PyPI
pip install proxycurl
```
* Make sure you set environtment `PROXYCURL_API_KEY` variable see `proxycurl/config.py`
* You can get `PROXYCURL_API_KEY` in [Proxycurl Official Web](https://nubela.co/proxycurl/auth/register)

## Example
After you install the library you can use like the example that provided each concurrent method:

### Gevent
```sh
# install required library
pip install 'proxycurl[gevent]'
python examples/lib-gevent.py
```
### Twisted
```sh
# install required library
pip install 'proxycurl[asyncio]'
python examples/lib-twisted.py
```
### Asyncio
```sh
# install required library
pip install 'proxycurl[asyncio]'
python examples/lib-asyncio.py
```

## For Development
To generate the library you must run this following command:
```sh
./codegen/generator
```
