import json
import csv
from route_var import RouteVar
from stop import Stop

class query:

    #_data should be a list of objects
    def __init__(self):
        self._list = []


    def push(self, element):
        self._list.append(element)

    def load(self, elements):
        for ele in elements:
            self._list.append(ele)

    def searchBy(self, att, cond):
        # cond - conditions - callback functions
        retList = []

        for element in self._list:
            if cond(element[att]):
                retList.append(element)

        return retList

    # _datas should be a list dictionary
    # fields is your list of headers
    def outputAsCSV(self, _datas, dest, fields):

        # print(fields)
        with open(dest, "w", newline="", encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in _datas:
                writer.writerow(row.__dict__)

        csvfile.close()

    def outputAsJSON(self, _datas, dest):
        with open(dest, "w", encoding="utf-8") as jsonfile:
            for obj in _datas:
                json.dump([obj.__dict__], jsonfile, ensure_ascii=False)
                jsonfile.write('\n')

        jsonfile.close()