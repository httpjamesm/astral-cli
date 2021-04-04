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
            print("[info] Upload Key: " + uploadKeyGET["data"] + " (use --regen-upkey to regenerate Upload Key.)")
    
    def changeSetting(self, setting, value):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }
        changeJSON = {
            setting: value
        }
        changeRequest = requests.patch(data.configdata["credentials"]["endpoint"] + "settings", headers=authorization, data=json.dumps(changeJSON))
        if changeRequest.status_code == 200:
            print("Successfully changed setting " + setting + " to value " + value + ".")
            return
