import json
import csv

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

    def outputAsCSV(self, _datas, dest): #CSV of stops
        # print(fields)
        if len(_datas) == 0:
            print("No data to write")
            return

        fields = _datas[0].get_keys()

        with open(dest, "w", newline="", encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in _datas:
                writer.writerow(row.__dict__)

        csvfile.close()
        print("file written at " + dest)

    def outputAsJSON(self, _datas, dest):
        if len(_datas) == 0:
            print("No data to write")
            return
        with open(dest, "w", encoding="utf-8") as jsonfile:
            for obj in _datas: # obj is a custom object with to_dict method
                # print(obj.to_dict())
                json.dump(obj.to_dict(), jsonfile, ensure_ascii=False)
                jsonfile.write('\n')

        jsonfile.close()
        print("file written at " + dest)

    def searchBy(self, atts, messageCond, className): #list att
        # atts is a list of attributes to be searched
        # conditions is a string that will be evaluated

        print(f"Calling {className}.SearchBy to Searching by {atts} with condition: {messageCond}")

        def cond(a, conditions):
            try:
                # Evaluate the condition string
                result = eval(conditions)
                if isinstance(result, bool):
                    return result
                else:
                    raise ValueError("Condition does not evaluate to a boolean value.")
            except Exception as e:
                print(f"Error occurred while evaluating the condition: {e}")
                return False

        # cond - conditions - callback functions
        retList = []

        for element in self._list:
            if cond([getattr(element, att) for att in atts], messageCond):
                retList.append(element)
        if (len(retList) == 0):
            print("No data found")

        return retList
