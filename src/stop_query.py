from stop import Stop
from query import query
import json
import csv

class RouteOfStop():
    def __init__(self, stops, RouteId, RouteVarId):
        self._stops = stops
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId

    @property
    def stops(self):
        return self._stops

    @property
    def RouteId(self):
        return self._RouteId

    @property
    def RouteVarId(self):
        return self._RouteVarId

    def to_dict(self):
        return {
            'stops': [stop.to_dict() for stop in self._stops],
            'RouteId': self._RouteId,
            'RouteVarId': self._RouteVarId
        }

class RouteOfStopQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        tmp = []
        with open(dest, "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)


                stopList = data["Stops"]
                _stopList = []
                for stop in stopList:
                    value_of_field = []
                    for v in stop:
                        value_of_field.append(stop[v])
                    _stopList.append(Stop(value_of_field))

                tmp.append(RouteOfStop(_stopList, data["RouteId"], data["RouteVarId"]))

        self._list = tmp

class StopQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        tmp = []
        with open(dest, "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)


                stopList = data["Stops"]
                for stop in stopList:
                    value_of_field = []
                    for v in stop:
                        value_of_field.append(stop[v])
                    tmp.append(Stop(value_of_field))
        self._list = tmp

test = StopQuery()
test.extract("../data/stops.json")
test.outputAsJSON(test._list, "test.json")

test2 = RouteOfStopQuery()
test2.extract("../data/stops.json")
test2.outputAsJSON(test2._list, "listStops.json")

def cond(listAtt):
    return listAtt[0] == "1" and listAtt[1] == "1"

f = test2.searchBy(["RouteId", "RouteVarId"], cond)

print(test2._list[0].RouteId)
print(len(f[0].stops))