import sys

from utils.domains import domains
from utils.accounts import accounts

class main():
    args = sys.argv[1:]
    if "--domains" in args:
        domains().getAllDomains()
    if "--login" in args:
        loginPos = args.index("--login")
        accounts().addToken(args[loginPos + 1])