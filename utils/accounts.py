# Libraries/Modules
import json
import requests
import pickle
import os
from dateutil import parser
import datetime as dt
import getpass
# Files
import utils.json as jsonutils
import data

class accounts():
    def addToken(self, username, password):
        # Store user credentials
    
        endpoint = input("Astral Endpoint (optional, must end in /): ")
        print(f'endpoint: {endpoint}')
        if not not endpoint:
            if list(endpoint)[-1] != "/":
                print("[x] Endpoint URL must end in a /.")
                return
        else:
            endpoint = "https://beta.astral.cool/"
        
        try:
            # Try to open the data.json file in write mode
            udfile = open("data.json", "xt")
        except:
            return
        
        # Template for user credentials
        dataTemplate = {
            "credentials": {
                "username": username,
                "password": password,
                "endpoint": endpoint,
                "encrypted": False
            }
        }
        try:
            # Try to write hte template to disk
            jsonutils.write_json(dataTemplate)
        except Exception as e:
            print("An unexpected error occured while logging into Astral.\n\n" + str(e))
            return
        
        print("[v] Account credentials successfully stored.\n[\] Getting Astral session data...")
        self.astralLogin()
        print("[\] Getting upload key...")
        self.getUploadKey()
        print("[v] We're done.")
        self.wipeLogin()

    def wipeLogin(self):
        # Delete username and password from disk for security
        
        with open("data.json", "r+") as dbfile:
            dbJSON = json.load(dbfile)
            del dbJSON["credentials"]["username"]
            del dbJSON["credentials"]["password"]
            dbfile.seek(0)
            dbfile.truncate(0)
            jsonutils.write_json(dbJSON)

    def editToken(self, username, password):
        # Edit username + password/relogin

        self.clearData()
        self.addToken(username, password)

    def astralLogin(self):
        # Get Astral session cookies and store them to disk
        
        try:
            # Check if the user stored their login credentials 
            dbfile = open("data.json", "r+")
        except Exception as e:
            print("You must add your credentials first! Use --login <username> <password>, and then run this command again.")
            return
        try:
            # Check if the database file is malformed
            dbJSON = json.load(dbfile)
        except:
            print("Malformed data.json file. Remove it and use --login <username> <password>, and then run this command again.")
            return
        
        try:
            # Try to acquire the credentials
            username = dbJSON["credentials"]["username"]
            password = dbJSON["credentials"]["password"]
        except:
            print("Credentials aren't present in data.json, did you run --login <username> <password>?")
            return

        # Create a new requests session to store cookies
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
                # Dump all session cookies to disk
                pickle.dump(loginSession.cookies, astralsession)
            print("[v] Logged in!")
            return
        print("[x] There was an error logging you in.\n\n" + loginResponse["message"])
    
    def getAccessToken(self):
        # Get the user's bearer/access token. This is required for almost all Astral requests.

        try:
            # Try to open the data.json file in read and write mode
            dbfile = open("data.json", "r+")
        except Exception as e:
            print("You must add your credentials first! Use --login <username> <password>, and then run this command again.")
            return
        try:
            # Check if the database file is malformed
            dbJSON = json.load(dbfile)
        except:
            print("Malformed data.json file. Remove it and use --login <username> <password>, and then run this command again.")
            return
        
        with open("astralsession.txt", "rb") as astralsession:
            # Load the session cookies
            cookies = pickle.load(astralsession)

        tokenPOST = requests.post(dbJSON["credentials"]["endpoint"] + "auth/login/token", data={}, cookies=cookies)
        
        responseJSON = json.loads(tokenPOST.content)
        return responseJSON["data"]["token"]

    def getUploadKey(self):
        # Get the user's upload key. This is required for uploading files to Astral.
        
        # Request headers with user access token
        authorization = {
            "Authorization": "Bearer " + self.getAccessToken(),
            "Content-Type": "application/json"
        }
        with open("data.json","r+") as dbfile:
            data.configdata = json.load(dbfile)
            uploadKeyGET = requests.get(data.configdata["credentials"]["endpoint"] + "settings/upload_key", headers=authorization)
            db = data.configdata
            db["credentials"]["uploadkey"] = json.loads(uploadKeyGET.content)["data"]
            dbfile.seek(0)
            dbfile.truncate(0)
            jsonutils.write_json(db)
        print("[v] Upload key stored.")
    
    def regenUploadKey(self):
        # Regenerate the user's upload key.

        print("[\] Regenerating upload key...")
        
        # Request headers with user access token
        try:
            authorization = {
                "Authorization": "Bearer " + self.getAccessToken(),
            }
        except:
            return
        try:
            uploadKeyPOST = requests.post(data.configdata["credentials"]["endpoint"] + "settings/upload_key", headers=authorization)
        except Exception as e:
            print("[x] An unexpected error occured while regenerating your upload key. Debug info below:\n\n" +str(e) + "\n\nJSON Response:\n" + str(uploadKeyPOST.content))
            return
        self.getUploadKey()
    
    def clearData(self):
        # Clear all account and session data locally.
        userChoice = input("Are you sure you want to irreversibly remove all local AstralCLI data? [y/N]: ")
        if userChoice.lower() == "y":
            print("[\] Clearing local data...")

            if os.path.exists("data.json"):
                os.remove("data.json")
            if os.path.exists("astralsession.txt"):
                os.remove("astralsession.txt")
            
            print("[\] All local data successfully removed.")
    
    def viewProfile(self, identifier):
        print(f"[\] Getting profile information for {{}}...\n".format(identifier))
        # Request headers with user access token
        authorization = {
            "Authorization": "Bearer " + self.getAccessToken(),
            "Content-Type": "application/json"
        }
        try:
            profileJSON = json.loads(requests.get(data.configdata["credentials"]["endpoint"] + "profiles/" + identifier, headers=authorization).content)
        except:
            return
            
        if profileJSON["code"] == "success":
            pairs = profileJSON["data"].items()
            profileList = []
            for item, value in pairs:
                if item == "registrationDate":
                    value = str(parser.parse(value))
                profileList.append(str(item + ": " + str(value)))
            print('\n'.join(profileList))
            return
        elif profileJSON["code"] == "not-found":
            print("[x] User not found.")
            return
        elif profileJSON["code"] == "invalid-token":
            print("[x] Invalid token. Did you modify the astralsession.txt file?\nUse --clear and re-login using --login.")
            return
        print(f"[x] An unexpected error occured. Debug info below:\n\n{{}}".format(profileJSON["code"]))
    
    def register(self):
        email = input("Email: ")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        passwordConf = getpass.getpass("Confirm Password: ")
        invite = input("Invite Code: ")
        eula = input("I accept Astral's EULA in its entirety [true/false]: ")

        if password != passwordConf:
            print("[x] Password mismatch.")
            return
        if eula.lower() != "true":
            print("[x] You cannot use Astral's services without accepting the EULA.")
            return
        
        endpoint = input("Astral Endpoint (optional, end URL with /): ")

        if not endpoint:
            endpoint = "https://beta.astral.cool/"
        else:
            if list(endpoint)[-1] != "/":
                print("[x] Your endpoint URL must end with a \"/\".")
                return
        headers = {
            "Content-Type": "application/json"
        }

        dataTemplate = {
            "email": email,
            "username": username,
            "password": password,
            "passwordConfirmation": passwordConf,
            "invite": invite,
            "eula": eula
        }

        try:
            registerRequest = requests.post(f"{endpoint}auth/register", headers=headers, data=json.dumps(dataTemplate)).json()
        except Exception as e:
            if "Invalid URL" in str(e):
                print(f"[x] An unexpected error occured while registering. Did you enter a valid endpoint URL? Debug info below\n\n{e}")
                return
            print(f"[x] An unexpected error occured while registering. Debug info below\n\n{e}")
            return
        
        if registerRequest["code"] == "success":
            print(f"[v] Astral account created successfully on endpoint {endpoint}. Login with your new credentials using --login <username> <password>.")
            return

        print(f"[x] An unexpected error occured registering to Astral endpoint {endpoint}. Debug info below:\n\n{registerRequest}")
