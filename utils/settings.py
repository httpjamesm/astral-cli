import requests
import json
# Files
import data
from utils.accounts import accounts

class settings():
    def viewAllSettings(self):
        # View all user settings and their values

        print("[\] Getting Astral settings...")
        # Request headers with user access token
        try:
            authorization = {
                "Authorization": "Bearer " + accounts().getAccessToken()
            }
        except:
            return
        settingsRequest = requests.get(data.configdata["credentials"]["endpoint"] + "settings", headers=authorization)
        if settingsRequest.status_code == 200:
            # If the request returns code 200 (OK)
            settingsResponse = settingsRequest.content
            settingsJSON = json.loads(settingsResponse)
            settingsJSON = settingsJSON["data"]
            pairs = settingsJSON.items()
            settingslist = []
            for setting,value in pairs:
                settingslist.append(str(setting + ": " + str(value)))
            # Get upload key
            uploadKeyGET = json.loads(requests.get(data.configdata["credentials"]["endpoint"] + "settings/upload_key", headers=authorization).content)
            # Get random domains list
            randomDomainsGET = json.loads(requests.get(data.configdata['credentials']['endpoint'] + "settings/random_domains", headers=authorization).content)
            settingslist.append("[info] Random domains: " + str(randomDomainsGET["data"]))
            settingslist.append("[info] Upload Key: " + uploadKeyGET["data"] + " (use --regen-upkey to regenerate)")
            print("\n" + '\n'.join(settingslist))
    
    def changeSetting(self, setting, value):
        # Change a user setting to a value

        # Request headers with user access token
        try:
            authorization = {
                "Authorization": "Bearer " + accounts().getAccessToken(),
                "Content-Type": "application/json"
            }
        except:
            return
        if setting == "selectedEmbedPreset":
            value = int(value)

        # Setting with new value
        changeJSON = {
            setting: value
        }
            
        changeRequest = requests.patch(data.configdata["credentials"]["endpoint"] + "settings", headers=authorization, data=json.dumps(changeJSON))
        responseJSON = json.loads(changeRequest.content)
        if responseJSON["code"] == "success":
            print("Successfully changed setting " + setting + " to value " + str(value) + ".")
            return
        if responseJSON["code"] == "bad-request" and responseJSON["message"] == "Invalid fields":
            print("[x] Invalid setting or setting value.")
            return
        print("[x] An unexpected error occured changing setting" + setting + " to value " + value + ".")
