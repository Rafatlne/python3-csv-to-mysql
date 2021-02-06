import csv
import json

# Read Json
class ReadJsonClass:
    
    def __init__(self, json_name):
        self.json_name = json_name

    def readJson(self):
        with open(self.json_name + '.json', encoding="utf8") as f:
            data = json.load(f)
            return data
