import json

def write_json(data, filename="data.json"):
    # Helper function to write json data to the db file
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
