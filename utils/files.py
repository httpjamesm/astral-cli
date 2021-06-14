import requests
import json

# Files
import data
import utils.json as jsonutils
from utils.accounts import accounts

class files():
    def viewFiles(self, page):
        # Request headers with the user access token
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken()
        }
        filesRequest = requests.get(data.configdata["credentials"]["endpoint"] + "files/" + str(page), headers=authorization).json()
        for x in filesRequest["data"]:
            fileList = []
            fileList.extend(["ID: " + x["id"], "Server Name: " + x["filename"], "Original Name: " + x["originalName"], "Size: " + str(round(x["size"]/1000000,2)) + " MB", "Timestamp: " + x["createdAt"], f"Deletion URL: {{}}files/delete?key={{}}".format(data.configdata["credentials"]["endpoint"], x["deletionKey"]),"\n"])
            print('\n'.join(fileList))