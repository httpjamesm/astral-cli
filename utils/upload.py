import requests, json, mimetypes

# Files

import utils.accounts
import data

class upload():
    def uploadFile(self, path):
        try:
            files = open(path,"rb")
        except:
            print("[x] Couldn't read file.")
            return
        
        authorization = {
            "api_key": data.configdata["credentials"]["uploadkey"]
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