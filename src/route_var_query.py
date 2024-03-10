from route_var import RouteVar
import csv

class RouteVarQuery:
    def __init__(self, routeVarList):
        self._list = routeVarList

    def pushRouteVar(self, routeVar):
        self._list.append(routeVar)

    def searchBy(self, att, cond):
        # cond - conditions - callback functions
        retList = []

        for element in self._list:
            if cond(element[att]):
                retList.append(element)

        return retList

    def outputAsCSV(sefl, _datas, dest, fields):
        print(fields)
        with open(dest, "w", newline="", encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in _datas:
                writer.writerow(row.__dict__)

        csvfile.close()
