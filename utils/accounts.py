# Libraries/Modules
import json, requests, pickle
# Files
import utils.json as jsonutils
import data

class accounts():
    def addToken(self, username, password):
        try:
            udfile = open("data.json", "xt")
        except:
            return
        
        dataTemplate = {
            "credentials": {
                "username": username,
                "password": password,
                "endpoint": "https://beta.astral.cool/"
            }
        }
        try:
            jsonutils.write_json(dataTemplate)
        except Exception as e:
            print("An unexpected error occured while logging into Astral.\n\n" + str(e))
            return
        
        print("Account token successfully added.")
    
    def editToken(self, token):
        with open("data.json", "r+") as dbfile:
            try:
                dataJSON = json.load(dbfile)
            except:
                print("Unexpected error while reading data.json file. Is the file corrupted? Remove it and try again.")

    def astralLogin(self):
        try:
            dbfile = open("data.json", "r+")
        except Exception as e:
            print("You must add your credentials first! Use --login <username> <password>, and then run this command again.")
            return
        try:
            dbJSON = json.load(dbfile)
        except:
            print("Malformed data.json file. Remove it and use --login <username> <password>, and then run this command again.")
            return
        
        try:
            username = dbJSON["credentials"]["username"]
            password = dbJSON["credentials"]["password"]
        except:
            print("Credentials aren't present in data.json, did you run --login <username> <password>?")
            return
        
        loginSession = requests.Session()
        loginRequestJSON = {
            "username": username,
            "password": password
        }
        requestHeaders = {
            "Content-Type": "application/json"
        }
        
        loginPOST = loginSession.post(dbJSON["credentials"]["endpoint"] + "auth/login", data=json.dumps(loginRequestJSON), headers=requestHeaders)
        loginResponse = json.loads(loginPOST.content)
        if loginResponse["code"] == "success":
            with open("astralsession.txt", "wb") as astralsession:
                pickle.dump(loginSession.cookies, astralsession)
            print("Logged in!")
            return
        print("[x] There was an error logging you in.\n\n" + loginResponse["message"])
    
    def getAccessToken(self):
        try:
            dbfile = open("data.json", "r+")
        except Exception as e:
            print("You must add your credentials first! Use --login <username> <password>, and then run this command again.")
            return
        try:
            dbJSON = json.load(dbfile)
        except:
            print("Malformed data.json file. Remove it and use --login <username> <password>, and then run this command again.")
            return
        
        try:
            username = dbJSON["credentials"]["username"]
            password = dbJSON["credentials"]["password"]
        except:
            print("Credentials aren't present in data.json, did you run --login <username> <password>?")
            return

        with open("astralsession.txt", "rb") as astralsession:
            cookies = pickle.load(astralsession)

        tokenPOST = requests.post(dbJSON["credentials"]["endpoint"] + "auth/login/token", data={}, cookies=cookies)
        
        responseJSON = json.loads(tokenPOST.content)
        return responseJSON["data"]["token"]

    def getUploadKey(self):
        authorization = {
            "Authorization": "Bearer " + self.getAccessToken(),
            "Content-Type": "application/json"
        }
        uploadKeyGET = requests.get(data.configdata["credentials"]["endpoint"] + "settings/upload_key", headers=authorization)
        db = data.configdata
        db["credentials"]["uploadkey"] = json.loads(uploadKeyGET.content)["data"]
        with open("data.json","r+") as dbfile:
            dbfile.seek(0)
            dbfile.truncate(0)
            jsonutils.write_json(db)
        print("Upload key stored.")