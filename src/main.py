# main to test the code
from route_var_query import RouteVarQuery
from route_var import RouteVar
import json

tmp = []
with open("../data/vars.json", "r", encoding="utf8") as file:
    for line in file:
        data = json.loads(line)

        for d in data:
            list = []
            for field in d:
                list.append(d[field])

            tmp.append(RouteVar(list))


myQuery = RouteVarQuery(tmp)
ls = myQuery._list[0].__dict__
fields = []
for field in ls:
    fields.append(field)
print(fields)
myQuery.outputAsCSV(myQuery._list, "test.csv", fields)