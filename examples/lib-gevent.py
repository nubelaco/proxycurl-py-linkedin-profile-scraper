from proxycurl.gevent import Proxycurl, do_bulk
import csv

proxycurl = Proxycurl()

balance = proxycurl.get_balance()

print('Balance:', balance)

person = proxycurl.linkedin.person.get(
    linkedin_profile_url='https://sg.linkedin.com/in/williamhgates'
)
print('Person Result:', person)

company = proxycurl.linkedin.company.get(
    url='https://www.linkedin.com/company/apple'
)
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
results = do_bulk(bulk_linkedin_person_data)

print('Bulk:', results)
