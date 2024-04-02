from unidecode import unidecode
import logging
from sub_modules.log_handler import Logger
from sub_modules import path_query, stop_query, route_var_query, promting_bot
import json

logger = Logger(__name__, level = logging.DEBUG, file_name="../logs/myapp.log")

class myApp:
    def __init__(self, dataPath):
        global logger
        self.pathQuery = path_query.PathQuery(logger)
        self.stopQuery = stop_query.StopQuery(logger)
        self.routeVarQuery = route_var_query.RouteVarQuery(logger)


        logger.info("Loading data into the app")
        self.pathQuery.extract(dataPath + "paths.json")
        self.stopQuery.extract(dataPath + "stops.json")
        self.routeVarQuery.extract(dataPath + "vars.json")
        logger.info("Data loaded")

        self.searchBot = promting_bot.respondHandler()

    def run(self):
        # print(self.stopQuery._list[0].name)
        # self.stopQuery.searchBy(["_name"], "fuzzy_compare(a[0], 'truong dai hoc khoa hoc tu nhien')", "stop")
        pass
    def option1(self):
        global logger

        logger.info("Option 1 selected")

        print("+========================================+")
        print("| Wellcome to the first search option!! |")
        print("+========================================+")
        message = input("Please enter the message: ")
        message = unidecode(message)
        response = self.searchBot.respond(message)
        print("------------------ respones ------------------")
        print(response)
        print("----------------------------------------------")
        response = json.loads(response)

        searchResult = []
        for obj in response:
            className = obj["class"]
            attributes = obj["attributes"]
            condition = obj["condition"]
            keyword = obj["keywordorname"]

            if (className == "stop"):
                searchResult = searchResult + self.stopQuery.searchBy(attributes, condition, className, keyword)
            elif (className == "routeVar"):
                searchResult = searchResult + self.routeVarQuery.searchBy(attributes, condition, className, keyword)

        name = input("what you want to name the output file: ")
        format = input("Please enter the format [csv, json]: ")

        if format == "csv":
            self.routeVarQuery.outputAsCSV(searchResult, "../output/" + name + ".csv")
        else:
            self.routeVarQuery.outputAsJSON(searchResult, "../output/" + name + ".json")

        logger.info("Option 1 completed")

    def option2(self):
        global logger

        logger.info("Option 2 selected")
        print("+========================================+")
        print("| Wellcome to the second search option!! |")
        print("+========================================+")
        print("class options: stop, routeVar")
        className = input("Please enter the class name: ")

        a = ""

        if (className == "stop"):
            print("Stop has these attributes: \n'_stopId', \n'_code', \n'_name', \n'_stopType', \n'_zone' (district), \n'_ward', \n'_addressNo', \n'_street', \n'_supportDisability', \n'_status', \n'_lng', \n'_lat', \n'_search', \n'_routes'")
            a = input("Please enter the attributes: ")
        elif (className == "routeVar"):
            print("RouteVar has these attributes: \n'_routeId', \n'_routeVarId', \n'_routeVarName', \n'_routeVarShortName', \n'_routeNo', \n'_startStop', \n'_endStop', \n'_distance', \n'_outBound', \n'_runningTime'")
            a = input("Please enter the attributes: ")

        condition = ""
        if (a in ['_name', '_routeVarName', '_routeVarShortName', '_ward', '_street', '_addressNo', '_zone']):
            query = input("Please enter name: ")
            condition = f"fuzzy_compare([x], '{query}')"
        else:
            condition = input("Please enter the condition, please use [x] as the variable: ")

        print(f"Searching by {a} with condition: {condition}")
        condition = condition.replace("[x]", f"a[0]", condition.count("[x]"))
        # print(f"Searching by {a} with condition: {condition}")

        searchResult = None
        if (className == "stop"):
            searchResult = self.stopQuery.searchBy([a], condition, className, [])
        elif (className == "routeVar"):
            searchResult = self.routeVarQuery.searchBy([a], condition, className, [])
        print(f"Found {len(searchResult)} results")
        name = input("what you want to name the output file: ")
        format = input("Please enter the format [csv, json]: ")

        if format == "csv":
            self.routeVarQuery.outputAsCSV(searchResult, "../output/" + name + ".csv")
        else:
            self.routeVarQuery.outputAsJSON(searchResult, "../output/" + name + ".json")

        logger.info("Option 2 completed")

    def option3(self):
        global logger

        logger.info("Option 3 selected")

        print("+======================================+")
        print("|      Welcome to the 3rd options      |")
        print("+======================================+")
        print("this option will output all the data of each class to csv and json files.")

        option = input("Please enter the class name ['stop', 'path', 'routeVar']: ")
        format = input("Please enter the format [csv, json]: ")
        name = input("what you want to name the output file: ")

        if option == "stop":
            if format == "csv":
                self.stopQuery.outputAsCSV(self.stopQuery._list, f"../output/{name}.csv")
            else:
                self.stopQuery.outputAsJSON(self.stopQuery._list, f"../output/{name}.json")
        elif option == "path":
            if format == "csv":
                self.pathQuery.outputAsCSV(self.pathQuery._list, f"../output/{name}.csv")
            else:
                self.pathQuery.outputAsJSON(self.pathQuery._list, f"../output/{name}.json")
        elif option == "routeVar":
            if format == "csv":
                self.routeVarQuery.outputAsCSV(self.routeVarQuery._list, f"../output/{name}.csv")
            else:
                self.routeVarQuery.outputAsJSON(self.routeVarQuery._list, f"../output/{name}.json")

        logger.info("Option 3 completed")

    def option4(self):
        global logger

        logger.info("Option 4 selected")

        print("+======================================+")
        print("|      Welcome to the 4th options      |")
        print("+======================================+")

        print("this option will plot the first path from the path.json on the map and output a geojson file.")

        import testGeoJson
        testGeoJson.run()

        print("Done!!")
        print("Please check the output file in the output folder.")
        print("you can use the geojson file to plot the path on the map of 'geojson.io'.")

        logger.info("Option 4 completed")

    def userInterface(self):
        global logger

        logger.info("User interface started")

        print("+======================================+")
        print("|          Welcome to the app          |")
        print("+======================================+")

        print("|__ This app allows you to search for stops, paths, and route variables!! __|")
        print("Please select an option:")
        print("[1]: search using prompting")
        print("[2]: search using select")
        print("[3]: output data to csv and json")
        print("[4]: play around with the geojson data")

        option = input("Your option: ")

        if option == "1":
            self.option1()
        elif option == "2":
            self.option2()
        elif option == "3":
            self.option3()
        elif option == "4":
            self.option4()

        logger.info("User interface completed")

if __name__ == "__main__":
    app = myApp("../data/")
    # load data into the
    app.run()
    app.userInterface()
    # app.search()
