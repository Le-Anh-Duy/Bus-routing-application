from sub_modules.path import Path
from sub_modules.query import query
import json

class PathQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        with open(dest, "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                self.push(Path([data["lat"], data["lng"], data["RouteId"], data["RouteVarId"]]))
        file.close()
        print("extracted path data")