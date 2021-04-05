#!/usr/bin/python3

import sys

from utils.domains import domains
from utils.accounts import accounts
from utils.settings import settings
from utils.upload import upload
from utils.embeds import embeds

class main():
    # Main file that receives CLI arguments.

    args = sys.argv[1:] # Get the arguments, not including the actual file name.

    if "--domains" in args:
        domains().getAllDomains()
    if "--login" in args:
        loginPos = args.index("--login")
        try:
            username = args[loginPos + 1]
            password = args[loginPos + 2]
        except:
            print("[x] Couldn't find username or password in your arguments.")
            exit()
        accounts().addToken(username, password)
    if "--settings" in args:
        settings().viewAllSettings()
    if "--change" in args:
        loginPos = args.index("--change")
        try:
            setting = args[loginPos + 1]
            value = args[loginPos + 2]
        except:
            print("[x] Couldn't find setting or value in your arguments.")
            exit()

        settings().changeSetting(setting, value)
    if "--upload" in args:
        argPos = args.index("--upload")
        try:
            upload().uploadFile(args[argPos + 1])
        except:
            print("[x] You must specify the path to a file you want to upload!")
            exit()
    if "--regen-upkey" in args:
        accounts().regenUploadKey()
    if "--add-random-domain" in args:
        argPos = args.index("--add-random-domain")
        domains().addRandomDomain(args[argPos + 1])
    if "--del-random-domain" in args:
        argPos = args.index("--del-random-domain")
        domains().delRandomDomain(args[argPos + 1])
    if "--embeds" in args:
        embeds().getAllEmbeds()
    if "--new-embed" in args:
        embeds().createNewEmbed()
    if "--del-embed" in args:
        argPos = args.index("--del-embed")
        embeds().deleteEmbedPreset(args[argPos + 1])
    if "--clear" in args:
        accounts().clearData()