from sub_modules import path_query, stop_query, route_var_query

class myApp:
    def __init__(self, dataPath):
        self.pathQuery = path_query.PathQuery()
        self.stopQuery = stop_query.StopQuery()
        self.routeVarQuery = route_var_query.RouteVarQuery()

        self.pathQuery.extract(dataPath + "paths.json")
        self.stopQuery.extract(dataPath + "stops.json")
        self.routeVarQuery.extract(dataPath + "vars.json")

    def run(self, destPath):
        self.pathQuery.outputAsCSV(self.pathQuery._list, destPath + "path.csv")
        self.routeVarQuery.outputAsCSV(self.routeVarQuery._list, destPath + "route_var.csv")
        self.stopQuery.outputAsCSV(self.stopQuery._list, destPath + "stop.csv")
        self.pathQuery.outputAsJSON(self.pathQuery._list, destPath + "path.json")
        self.routeVarQuery.outputAsJSON(self.routeVarQuery._list, destPath + "route_var.json")
        self.stopQuery.outputAsJSON(self.stopQuery._list, destPath + "stop.json")
        pass

    def search(self):
        print(len(self.routeVarQuery.searchBy(["_runningTime", "_distance"], "a[0] < 100 and a[1] < 50000", "routeVar")))
#{"class": "routeVar", "attributes": ["_runningTime", "_distance"], "condition": "a[0] < 10 and a[1] < 5"}

if __name__ == "__main__":
    # load data into the app
    app = myApp("../data/")


    app.run("../output/")
    app.search()
