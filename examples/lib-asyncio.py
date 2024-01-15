import asyncio
from proxycurl.asyncio import Proxycurl, do_bulk
import csv

proxycurl = Proxycurl()


balance = asyncio.run(proxycurl.get_balance())

print('Balance:', balance)

person = asyncio.run(proxycurl.linkedin.person.get(
    linkedin_profile_url='https://sg.linkedin.com/in/williamhgates'
))

print('Person Result:', person)

company = asyncio.run(proxycurl.linkedin.company.get(
    url='https://www.linkedin.com/company/apple'
))

print('Company Result:', company)

# PROCESS BULK WITH CSV
bulk_linkedin_person_data = []
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        bulk_linkedin_person_data.append(
            (proxycurl.linkedin.person.get, {'linkedin_profile_url': row[0]})
        )
results = asyncio.run(do_bulk(bulk_linkedin_person_data))

print('Bulk:', results)
