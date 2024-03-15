from stop import Stop
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
