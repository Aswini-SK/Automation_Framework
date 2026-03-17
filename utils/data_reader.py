import json

def read_json(file):
    with open(file) as f:
        return json.load(f)