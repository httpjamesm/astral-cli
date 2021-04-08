import json

try:
    with open("data.json", "r") as dbfile:
        configdata = json.load(dbfile)
except Exception as e:
    print(e)