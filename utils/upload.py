import requests, json, mimetypes, os

# Files

import utils.accounts
import data

class upload():
    def uploadFile(self, path):
        if os.path.getsize(path) > 100000000:
            userChoice = input("[?] The file you're trying to upload is above Astral's 100mb upload limit. Do you wish to override? [y/N]: ")
            if userChoice.lower() == "n":
                print("[x] Cancelling upload...")
                return
            print("[v] Overriding local file size check...")
        
        print("[\] Uploading file " + path + "...")
        try:
            files = open(path,"rb")
        except:
            print("[x] Couldn't read file.")
            return
        
        authorization = {
            "Authorization": data.configdata["credentials"]["uploadkey"]
        }
        files = {
            "file": (files.name, files, mimetypes.guess_type(path)[0])
        }
        uploadRequest = requests.post(data.configdata["credentials"]["endpoint"] + "files", files=files, headers=authorization)
        try:
            responseJSON = json.loads(uploadRequest.content)
        except Exception as e:
            print("[x] Received unexpected response from Astral API. Debug info below:\n\n" + str(e) + "\n\nJSON Response:\n" + str(uploadRequest.content))
            return
        if responseJSON["code"] == "success":
            print("Upload URL: " + responseJSON["fileURL"] + "\nDelete URL: " + responseJSON["deletionURL"])
        else:
            print("[x] Error uploading file.\n")
            if responseJSON["message"] == "Invalid mimetype":
                print("Invalid file type. Did you try to upload a disallowed file?")
            elif responseJSON["message"] == "The provided upload key does not exist":
                print("Invalid API key. Did you edit your key in data.json?")