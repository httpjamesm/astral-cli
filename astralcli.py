import sys

from utils.domains import domains
from utils.accounts import accounts
from utils.settings import settings

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
