import requests
import json

# Files
import data
import utils.json as jsonutils
from utils.accounts import accounts

class files():
    def viewFiles(self, page):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken()
        }
        filesRequest = requests.get(data.configdata["credentials"]["endpoint"] + "files/" + str(page), headers=authorization).json()
        for x in filesRequest["data"]:
            fileList = []
            fileList.extend(["ID: " + x["id"], "Server Name: " + x["filename"], "Original Name: " + x["originalName"], "Size (MB): " + str(x["size"]/10000), "Timestamp: " + x["createdAt"], f"Deletion URL: {{}}files/delete?key={{}}".format(data.configdata["credentials"]["endpoint"], x["deletionKey"]),"\n"])
            print('\n'.join(fileList))