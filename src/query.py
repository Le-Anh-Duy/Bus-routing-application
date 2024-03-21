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

        # _datas should be a list dictionary
    # fields is your list of headers
    def outputAsCSV(self, _datas, dest, fields): #CSV of stops
        # print(fields)
        with open(dest, "w", newline="", encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in _datas:
                writer.writerow(row.__dict__)

        csvfile.close()

    def outputAsJSON(self, _datas, dest):
        with open(dest, "w", encoding="utf-8") as jsonfile:
            for obj in _datas: # obj is a custom object with to_dict method
                # print(obj.to_dict())
                json.dump(obj.to_dict(), jsonfile, ensure_ascii=False)
                jsonfile.write('\n')

        jsonfile.close()

    def searchBy(self, atts, cond): #list att
        # cond - conditions - callback functions
        retList = []

        for element in self._list:
            if cond([getattr(element, att) for att in atts]):
                retList.append(element)

        return retList