import requests,json

#Files
from utils.accounts import accounts
import data

class embeds():
    def getAllEmbeds(self):
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken()
        }
        embedRequest = requests.get(data.configdata["credentials"]["endpoint"] + "settings/embeds", headers=authorization)
        responseJSON = json.loads(embedRequest.content)
        counter = 0
        for preset in responseJSON["data"]:
            print("\nEmbed Preset #" + str(counter + 1) + ":\n")
            pairs = responseJSON["data"][counter].items()
            for setting,value in pairs:
                print(str(setting + ": " + str(value)))
            counter += 1

    def createNewEmbed(self):
        title = input("Title: ")
        description = input("Description: ")
        author = input("Author: ")
        domain = input("Site: ")
        color = input("Color: ")
        randomColor = input("Random Embed Color [true/false]: ")
        if randomColor.lower() not in ["true","false"]:
            print("[x] Invalid choice for random color.")
            return

        dataTemplate = {
            "title": title,
            "description": description,
            "author": author,
            "site": domain,
            "color": color,
            "randomColor": randomColor
        }

        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }

        embedRequest = requests.put(data.configdata["credentials"]["endpoint"] + "settings/embeds", headers=authorization, data=json.dumps(dataTemplate))
        embedJSON = json.loads(embedRequest.content)
        if embedJSON["code"] == "success":
            print("[v] Successfully created embed preset.")
            return
        elif embedJSON["code"] == "limit-reached":
            print("[x] You have too many embed presets. Delete one first before creating a new one.")
            return
        else:
            print("[x] An unknown error occured. Debug info below:\n\n")
            print(embedJSON)
            return

    def editEmbedPreset(self, number: int):
        title = input("Title: ")
        description = input("Description: ")
        author = input("Author: ")
        domain = input("Site: ")
        color = input("Color: ")
        randomColor = input("Random Embed Color [true/false]: ").lower()
        if randomColor not in ["true","false"]:
            print("[x] Invalid choice for random color.")
            return

        dataTemplate = {
            "title": title,
            "description": description,
            "author": author,
            "site": domain,
            "color": color,
            "randomColor": randomColor
        }

        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken(),
            "Content-Type": "application/json"
        }

        editRequest = requests.patch(data.configdata["credentials"]["endpoint"] + "settings/embeds/"+ str(number), headers=authorization, data=dataTemplate).json()

        if editRequest["code"] == "success":
            print("[v] Successfully edited embed preset.")
            return
    
    def deleteEmbedPreset(self, number):
        try:
            number = int(number)
        except:
            print("[x] Invalid integer.")
            return
        
        authorization = {
            "Authorization": "Bearer " + accounts().getAccessToken()
        }
        deleteRequest = requests.delete(data.configdata["credentials"]["endpoint"] + "settings/embeds/" + str(number), headers=authorization)
        requestJSON = json.loads(deleteRequest.content)
        if requestJSON["code"] == "success":
            print("[v] Embed " + str(number) + " has been deleted.")
            return
        print("[x] An unknown error occured. Debug info below:\n\n" + str(requestJSON))
