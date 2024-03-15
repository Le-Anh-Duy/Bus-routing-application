# # main to test the code
from route_var_query import RouteVarQuery
from route_var import RouteVar
import json
from query import query

tmp = [] #list of vars
with open("../data/vars.json", "r", encoding="utf8") as file:
    for line in file:
        data = json.loads(line)
        for d in data: # d is a dict
            value_of_field = []
            for v in d:
                value_of_field.append(d[v])
            print(value_of_field)

        tmp.append(RouteVar(value_of_field))



myQuery = query()
myQuery.load(tmp)
myQuery.outputAsCSV(myQuery._list, "test01.csv", tmp[0].get_keys())
myQuery.outputAsJSON(myQuery._list, "test01.json")