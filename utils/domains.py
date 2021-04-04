import requests, json

# Files
import data

class domains():
    def getAllDomains(self):
        domainsRequest = requests.get(data.configdata["credentials"]["endpoint"] + "domains")
        if domainsRequest.status_code == 200:
            domainsResponse = domainsRequest.content
            domainsJSON = json.loads(domainsResponse)
            domainsList = []
            num = 1
            for domain in domainsJSON['data']['domains']:
                domainsList.append(str(num) + ". " + domain['name'])
                num += 1
            print('\n'.join(domainsList))
        else:
            print(domainsRequest.content)
