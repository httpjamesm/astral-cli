import requests, json

class domains():
    def getAllDomains(self):
        domainsRequest = requests.get('https://beta.astral.cool/domains/')
        if domainsRequest.status_code == 200:
            domainsResponse = domainsRequest.content
            domainsJSON = json.loads(domainsResponse)
            domainsList = []
            for domain in domainsJSON['data']['domains']:
                domainsList.append(domain['name'])
            print('\n'.join(domainsList))
