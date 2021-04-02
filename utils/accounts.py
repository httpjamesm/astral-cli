import json

import utils.json as jsonutils

class accounts():
    def addToken(self,token):
        try:
            udfile = open("data.json", "xt")
        except:
            #self.editToken(token)
            return
        
        dataTemplate = {
            "credentials": {
                "userToken": token,
                "endpoint": "https://beta.astral.cool/"
            }
        }
        try:
            jsonutils.write_json(dataTemplate)
        except Exception as e:
            print("An unexpected error occured while logging into Astral.\n\n" + str(e))
            return
        
        print("Account token successfully added.")

