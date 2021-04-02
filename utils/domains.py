import requests, json

class domains():
    def getAllDomains(self):
        domainsRequest = requests.get('https://beta.astral.cool/domains/')
        if domainsRequest.status_code == 200:
            domainsResponse = domainsRequest.content
            domainsJSON = json.loads(domainsResponse)
            domainsList = []
            num = 1
            for domain in domainsJSON['data']['domains']:
                domainsList.append(str(num) + ". " + domain['name'])
                num += 1
            print('\n'.join(domainsList))
