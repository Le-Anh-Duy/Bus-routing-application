from path import path
from query import query
import json

class path_query(query):
    def __init__(self):
        super().__init__()

    def extract(self):
        with open("../../data/paths.json", "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                self.push(path([data["lat"], data["lng"], data["RouteId"], data["RouteVarId"]]))
# Path: src/query.py
            file.close()

tmp = path_query()
tmp.extract()
print(tmp._list[0]._lat)
print(tmp._list[0]._lng)