import requests, json

# Files
import data
from utils.accounts import accounts

class domains():
    def getAllDomains(self):
        domainsRequest = requests.get(data.configdata["credentials"]["endpoint"] + "domains/list")
        print(domainsRequest.content)
        if domainsRequest.status_code == 200:
            domainsResponse = domainsRequest.content
            domainsJSON = json.loads(domainsResponse)
            domainsList = []
            num = 1
            for domain in domainsJSON['data']['domains']:
                domainsList.append(str(num) + ". " + domain)
                num += 1
            print('\n'.join(domainsList))
        else:
            print(domainsRequest.content)
    
    def addRandomDomain(self, domain):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }
        request = {
            "domain": domain
        }
        rdRequest = json.loads(requests.put(data.configdata["credentials"]["endpoint"] + "settings/random_domains", headers=authorization, data=json.dumps(request)).content)
        if rdRequest["code"] == "success":
            print("[v] Domain " + domain + " added successfully.")
            return
        print("[x] An unexpected error occured adding domain " + domain + ".")        

    def delRandomDomain(self, domain):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }
        request = {
            "domain": domain
        }
        rdRequest = json.loads(requests.delete(data.configdata["credentials"]["endpoint"] + "settings/random_domains/" + domain, headers=authorization, data=json.dumps(request)).content)
        if rdRequest["code"] == "success":
            print("[v] Domain " + domain + " deleted successfully.")
            return
        print("[x] An unexpected error occured deleting domain " + domain + ".")     
        print(rdRequest)   
