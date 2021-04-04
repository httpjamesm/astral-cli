#!/usr/bin/python3

import sys

from utils.domains import domains
from utils.accounts import accounts
from utils.settings import settings
from utils.upload import upload

class main():
    args = sys.argv[1:]
    if "--domains" in args:
        domains().getAllDomains()
    if "--login" in args:
        loginPos = args.index("--login")
        username = args[loginPos + 1]
        password = args[loginPos + 2]
        accounts().addToken(username, password)
    if "--settings" in args:
        settings().viewAllSettings()
    if "logintoastral" in args:
        accounts().astralLogin()
    if "gettoken" in args:
        accounts().getAccessToken()
    if "--change" in args:
        loginPos = args.index("--change")
        setting = args[loginPos + 1]
        value = args[loginPos + 2]
        settings().changeSetting(setting, value)
    if "--uploadkey" in args:
        accounts().getUploadKey()
    if "--upload" in args:
        argPos = args.index("--upload")
        upload().uploadFile(args[argPos + 1])
    if "--regen-upkey" in args:
        accounts().regenUploadKey()
    if "--add-random-domain" in args:
        argPos = args.index("--add-random-domain")
        domains().addRandomDomain(args[argPos + 1])
    if "--del-random-domain" in args:
        argPos = args.index("--del-random-domain")
        domains().delRandomDomain(args[argPos + 1])
