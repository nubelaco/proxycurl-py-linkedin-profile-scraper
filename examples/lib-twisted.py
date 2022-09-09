from proxycurl.twisted import Proxycurl, do_bulk
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import csv

proxycurl = Proxycurl()

@inlineCallbacks
def main():
    balance = yield proxycurl.get_balance()
    print('Balance:', balance)


    person = yield proxycurl.linkedin.person.get(
        url='https://sg.linkedin.com/in/williamhgates'
    )

    print('Person:', person)

    company = yield proxycurl.linkedin.company.get(
        url='https://www.linkedin.com/company/apple'
    )

    print('Company:', company)

    # PROCESS BULK WITH CSV
    bulk_linkedin_person_data = []
    with open('sample.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            bulk_linkedin_person_data.append(
                (proxycurl.linkedin.person.get, {'url': row[0]})
            )
    bulk = yield do_bulk(bulk_linkedin_person_data)

    print('Bulk:', bulk)

    reactor.stop()

main()

reactor.run()