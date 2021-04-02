import sys

from utils.domains import domains

class main():
    args = sys.argv[1:]
    if "--domains" in args:
        domains().getAllDomains()