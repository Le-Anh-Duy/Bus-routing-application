from sub_modules.query import query
from sub_modules.route_var import RouteVar
import json

class RouteVarQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        tmp = []
        with open(dest, "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                for d in data: # d is a dict
                    value_of_field = []
                    for v in d:
                        value_of_field.append(d[v])


                tmp.append(RouteVar(value_of_field))
        self._list = tmp
        file.close()

        print("extracted route_var data")