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