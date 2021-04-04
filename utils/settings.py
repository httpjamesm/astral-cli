import requests, json
# Files
import data
from utils.accounts import accounts

class settings():
    def viewAllSettings(self):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken()
        }
        settingsRequest = requests.get(data.configdata["credentials"]["endpoint"] + "settings", headers=authorization)
        if settingsRequest.status_code == 200:
            settingsResponse = settingsRequest.content
            settingsJSON = json.loads(settingsResponse)
            settingsJSON = settingsJSON["data"]
            pairs = settingsJSON.items()
            for setting,value in pairs:
                print(str(setting + ": " + str(value)))
            uploadKeyGET = json.loads(requests.get(data.configdata["credentials"]["endpoint"] + "settings/upload_key", headers=authorization).content)
            randomDomainsGET = json.loads(requests.get(data.configdata['credentials']['endpoint'] + "settings/random_domains", headers=authorization).content)
            print("[info] Random domains: " + str(randomDomainsGET["data"]))
            print("[info] Upload Key: " + uploadKeyGET["data"] + " (use --regen-upkey to regenerate)")
    
    def changeSetting(self, setting, value):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }
        changeJSON = {
            setting: value
        }
        changeRequest = requests.patch(data.configdata["credentials"]["endpoint"] + "settings", headers=authorization, data=json.dumps(changeJSON))
        responseJSON = json.loads(changeRequest.content)
        if responseJSON["code"] == "success":
            print("Successfully changed setting " + setting + " to value " + value + ".")
            return
        if responseJSON["code"] == "bad-request" and responseJSON["message"] == "Invalid fields":
            print("[x] Invalid setting or setting value.")
            return
        print("[x] An unexpected error occured changing setting" + setting + " to value " + value + ".")
