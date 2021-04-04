import requests, json

# Files
import data
from utils.accounts import accounts

class domains():
    def getAllDomains(self):
        # Parse the public Astral domain list.

        # GET request the domains list using the configured endpoint
        domainsRequest = requests.get(data.configdata["credentials"]["endpoint"] + "domains/list")
        if domainsRequest.status_code == 200:
            # If the request returns a 200 (OK) status code
            domainsResponse = domainsRequest.content
            domainsJSON = json.loads(domainsResponse)
            domainsList = []
            num = 1
            for domain in domainsJSON['data']['domains']:
                # Enumerate the domains list
                domainsList.append(str(num) + ". " + domain)
                num += 1
            print('\n'.join(domainsList))
        else:
            print(domainsRequest.content)
    
    def addRandomDomain(self, domain):
        # Add a random domain to the user's random domain list

        # Request headers with user access token
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
        # Delete a random domain frmo the user's random domain list

        # Request headers with the user access token
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
