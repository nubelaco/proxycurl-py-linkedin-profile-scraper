# `proxycurl-py` -  The official Python client for Proxycurl API to scrape and enrich LinkedIn profiles

* [What is Proxycurl?](#what-is-proxycurl-)
* [Before you install](#before-you-install)
* [Installation and supported Python versions](#installation-and-supported-python-versions)
* [Initializing `proxycurl-py` with an API Key](#initializing--proxycurl-py--with-an-api-key)
* [Usage with examples](#usage-with-examples)
  + [Enrich a Person Profile](#enrich-a-person-profile)
  + [Enrich a Company Profile](#enrich-a-company-profile)
  + [Lookup a person](#lookup-a-person)
  + [Lookup a company](#lookup-a-company)
  + [Lookup a LinkedIn Profile URL from a work email address](#lookup-a-linkedin-profile-url-from-a-work-email-address)
  + [Enrich LinkedIn member profiles in bulk (from a CSV)](#enrich-linkedin-member-profiles-in-bulk--from-a-csv-)
  + [More *asyncio* examples](#more--asyncio--examples)
* [Rate limit and error handling](#rate-limit-and-error-handling)
* [API Endpoints and their corresponding documentation](#api-endpoints-and-their-corresponding-documentation)

## What is Proxycurl?

**Proxycurl** is an enrichment API to fetch fresh data on people and businesses. We are a fully-managed API that sits between your application and raw data so that you can focus on building the application; instead of worrying about building a web-scraping team and processing data at scale.

With Proxycurl, you can programatically:

- Enrich profiles on people and companies
- Lookup people and companies
- Lookup contact information on people and companies
- Check if an email address is of a disposable nature
- [And more..](https://nubela.co/proxycurl/docs#explain-it-to-me-like-i-39-m-5)

Visit [Proxycurl&#39;s website](https://nubela.co/proxycurl) for more details.

## Before you install

You should understand that `proxycurl-py` was designed with concurrency as a first class citizen from ground-up. To install `proxycurl-py`, *you have to pick a concurency model*.

We support the following concurrency models:

* [asyncio](https://docs.python.org/3/library/asyncio.html) - See implementation example [here](https://github.com/nubelaco/proxycurl-linkedin-scraper/blob/main/examples/lib-asyncio.py).
* [gevent](https://www.gevent.org/) - See implementation example [here](https://github.com/nubelaco/proxycurl-linkedin-scraper/blob/main/examples/lib-gevent.py).
* [twisted](https://twisted.org/) - See implementation example [here](https://github.com/nubelaco/proxycurl-linkedin-scraper/blob/main/examples/lib-twisted.py).

The right way to use Proxycurl API is to make API calls concurrently. In fact, making API requests concurrently is the only way to achieve a high rate of throughput. On the default rate limit, you can enrich up to 432,000 profiles per day. See [this blog post](https://nubela.co/blog/how-to-maximize-throughput-on-proxycurl/) for context.

## Installation and supported Python versions

`proxycurl-py` is [available on PyPi](https://pypi.org/project/proxycurl/). For which you can install into your project with the following command:

```bash
# install proxycurl-py with asyncio
$ pip install 'proxycurl-py[asyncio]'

# install proxycurl-py with gevent
$ pip install 'proxycurl-py[gevent]'

# install proxycurl-py with twisted
$ pip install 'proxycurl-py[twisted]'
```

`proxycurl-py` is tested on Python `3.7`, `3.8` and `3.9`.

## Initializing `proxycurl-py` with an API Key

You can get an API key by [registering an account](https://nubela.co/proxycurl/auth/register) with Proxycurl. The API Key can be retrieved from the dashboard.

To use Proxycurl with the API Key:

* You can run your script with  the `PROXYCURL_API_KEY` environment variable set.
* Or, you can prepend your script with the API key injected into the environment. See `proxycurl/config.py` for an example.

## Usage with examples

I will be using `proxycurl-py` with the *asyncio* concurrency model to illustrate some examples on what you can do with Proxycurl and how the code will look with this library.

Forexamples with other concurrency models such as:

* *gevent*, see `examples/lib-gevent.py`.
* *twisted*, see `examples/lib-twisted`.

### Enrich a Person Profile

Given a *LinkedIn Member Profile URL*, you can get the entire profile back in structured data with Proxycurl's [Person Profile API Endpoint](https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint).

```python
from proxycurl_py.asyncio import Proxycurl, do_bulk
import asyncio
import csv

proxycurl = Proxycurl()
person = asyncio.run(proxycurl.linkedin.person.get(
    url='https://www.linkedin.com/in/williamhgates/'
))
print('Person Result:', person)
```

### Enrich a Company Profile

Given a *LinkedIn Company Profile URL*, enrich the URL with it's full profile with Proxycurl's [Company Profile API Endpoint](https://nubela.co/proxycurl/docs#company-api-company-profile-endpoint).

```python
company = asyncio.run(proxycurl.linkedin.company.get(
    url='https://www.linkedin.com/company/tesla-motors'
))
print('Company Result:', company)
```

### Lookup a person

Given a first name and a company name or domain, lookup a person with Proxycurl's [Person Lookup API Endpoint](https://nubela.co/proxycurl/docs#people-api-person-lookup-endpoint).

```python
lookup_results = asyncio.run(proxycurl.linkedin.person.resolve(first_name="bill", last_name="gates", company_domain="microsoft"))
print('Person Lookup Result:', lookup_results)
```

### Lookup a company

Given a company name or a domain, lookup a company with Proxycurl's [Company Lookup API Endpoint](https://nubela.co/proxycurl/docs#company-api-company-lookup-endpoint).

```python
company_lookup_results = asyncio.run(proxycurl.linkedin.company.resolve(company_name="microsoft", company_domain="microsoft.com"))
print('Company Lookup Result:', company_lookup_results)
```

### Lookup a LinkedIn Profile URL from a work email address

Given a work email address, lookup a LinkedIn Profile URL with Proxycurl's [Reverse Work Email Lookup Endpoint](https://nubela.co/proxycurl/docs#contact-api-reverse-work-email-lookup-endpoint).

```python
lookup_results = asyncio.run(proxycurl.linkedin.person.resolve_by_email(work_email="anthony.tan@grab.com"))
print('Reverse Work Email Lookup Result:', lookup_results)
```

### Enrich LinkedIn member profiles in bulk (from a CSV)

Given a CSV file with a list of LinkedIn member profile URLs, you can enrich the list in the following manner:

```python
# PROCESS BULK WITH CSV
bulk_linkedin_person_data = []
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        bulk_linkedin_person_data.append(
            (proxycurl.linkedin.person.get, {'url': row[0]})
        )
results = asyncio.run(do_bulk(bulk_linkedin_person_data))

print('Bulk:', results)
```

### More *asyncio* examples

More *asyncio* examples can be found at `examples/lib-asyncio.py`

## Rate limit and error handling

There is no need for you to handle rate limits (`429` HTTP status error). The [library handles rate limits automatically with exponential backoff](https://github.com/nubelaco/proxycurl-linkedin-scraper/blob/main/proxycurl/asyncio/base.py#L109).

However, there is a need for you to handle other error codes. Errors will be returned in the form of `ProxycurlException`. The [list of possible errors](https://nubela.co/proxycurl/docs#overview-errors) is listed in our API documentation.

## API Endpoints and their corresponding documentation

Here we list the possible API endpoints and their corresponding library functions. Do refer to each endpoint's relevant API documentation to find out the required arguments that needs to be fed into the function.

| Function                                       | Endpoint                                                                                                                     | API                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `linkedin.company.employee_count(**kwargs)`  | [Employee Count Endpoint](https://nubela.co/proxycurl/docs#company-api-employee-count-endpoint)                                 | [Company API](https://nubela.co/proxycurl/docs#company-api) |
| `linkedin.company.resolve(**kwargs)`         | [Company Lookup Endpoint](https://nubela.co/proxycurl/docs#company-api-company-profile-endpoint)                                | [Company API](https://nubela.co/proxycurl/docs#company-api) |
| `linkedin.company.employee_list(**kwargs)`   | [Employee Listing Endpoint](https://nubela.co/proxycurl/docs#company-api-employee-listing-endpoint)                             | [Company API](https://nubela.co/proxycurl/docs#company-api) |
| `linkedin.company.get(**kwargs)`             | [Company Profile Endpoint](https://nubela.co/proxycurl/docs#company-api-company-profile-endpoint)                               | [Company API](https://nubela.co/proxycurl/docs#company-api) |
| `linkedin.person.resolve_by_email(**kwargs)` | [Reverse Work Email Lookup Endpoint](https://nubela.co/proxycurl/docs#contact-api-reverse-work-email-lookup-endpoint)           | [Contact API](https://nubela.co/proxycurl/docs#contact-api) |
| `linkedin.person.lookup_email(**kwargs)`     | [Work Email Lookup Endpoint](https://nubela.co/proxycurl/docs#contact-api-work-email-lookup-endpoint)                           | [Contact API](https://nubela.co/proxycurl/docs#contact-api) |
| `linkedin.person.personal_contact(**kwargs)` | [Personal Contact Number Lookup Endpoint](https://nubela.co/proxycurl/docs#contact-api-personal-contact-number-lookup-endpoint) | [Contact API](https://nubela.co/proxycurl/docs#contact-api) |
| `linkedin.person.personal_email(**kwargs)`   | [Personal Email Lookup Endpoint](https://nubela.co/proxycurl/docs#contact-api-personal-email-lookup-endpoint)                   | [Contact API](https://nubela.co/proxycurl/docs#contact-api) |
| `linkedin.disposable_email(**kwargs)`        | [Disposable Email Address Check Endpoint](https://nubela.co/proxycurl/docs#contact-api-disposable-email-address-check-endpoint) | [Contact API](https://nubela.co/proxycurl/docs#contact-api) |
| `linkedin.company.find_job(**kwargs)`        | [Job Listings Endpoint](https://nubela.co/proxycurl/docs#jobs-api-jobs-listing-endpoint)                                        | [Jobs API](https://nubela.co/proxycurl/docs#jobs-api)       |
| `linkedin.job.get(**kwargs)`                 | [Jobs Profile Endpoint](https://nubela.co/proxycurl/docs#jobs-api-job-profile-endpoint)                                         | [Jobs API](https://nubela.co/proxycurl/docs#jobs-api)       |
| `linkedin.person.resolve(**kwargs)`          | [Person Lookup Endpoint](https://nubela.co/proxycurl/docs#people-api-person-lookup-endpoint)                                    | [People API](https://nubela.co/proxycurl/docs#people-api)   |
| `linkedin.company.role_lookup(**kwargs)`     | [Role Lookup Endpoint](https://nubela.co/proxycurl/docs#people-api-role-lookup-endpoint)                                        | [People API](https://nubela.co/proxycurl/docs#people-api)   |
| `linkedin.person.get(**kwargs)`              | [Person Profile Endpoint](https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint)                                  | [People API](https://nubela.co/proxycurl/docs#people-api)   |
| `linkedin.school.get(**kwargs)`              | [School Profile Endpoint](https://nubela.co/proxycurl/docs#school-api-school-profile-endpoint)                                  | [School API](https://nubela.co/proxycurl/docs#school-api)   |
| `linkedin.company.reveal`                    | [Reveal Endpoint](https://nubela.co/proxycurl/docs#reveal-api-reveal-endpoint)                                                  | [Reveal API](https://nubela.co/proxycurl/docs#reveal-api)   |
| `get_balance(**kwargs)`                      | [View Credit Balance Endpoint](https://nubela.co/proxycurl/docs#meta-api-view-credit-balance-endpoint)                          | [Meta API](https://nubela.co/proxycurl/docs#meta-api)       |
