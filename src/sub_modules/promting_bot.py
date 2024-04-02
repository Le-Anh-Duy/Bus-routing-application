import anthropic
import dotenv
import os

class respondHandler():
    def __init__(self):
        self.stopData = '<className>stop</className> has these attributes: <listAttributes>"_stopId", "_code", "_name", "_stopType", "_zone", "_ward", "_addressNo", "_street", "_supportDisability", "_status", "_lng", "_lat", "_search", "_routes"</listAttributes>'
        self.routeVarData = '<className>routeVar</className> has these attributes: <listAttributes>"_routeId", "_routeVarId","_routeVarName","_routeVarShortName","_routeNo","_startStop","_endStop","_distance","_outBound","_runningTime"</listAttributes>'

        dotenv.load_dotenv()
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(
            api_key=anthropic_api_key,
        )

    def respond(self, messages):

        print(f"responding, please wait...")

        message = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.0,
            system = f'given the data [{self.routeVarData}, {self.stopData}]. Return the class, the list of keyword or name that should be considered, the list of attribute named "attributes" that are used in condition and the condition string that python can understand, the i-th attribute in the "attributes" should be a[i] in the condition string, with "i" is the index of that attribute in the "attributes", starting from 0, respond only in json format in one line. For example if the message is "find me stop with support disable and near benh vien nhiet doi"' + ' you should respond with [{"class": "stop", "keywordorname": ["benh vien nhiet doi"], "attributes": ["_supportDisability"], "condition": "a[0] == True"}]" + " when in the condition requires to make string comparision, please use the "fuzzy_compare(string_1, string_2)" functions to compare the string, for example "fuzzy_compare(a[0], \'asdfdsfs\') == True", when dealing with address or name, please put them on the "keywordorname" list but still put the attribute in the "attributes" list, for example "find me stop with name benh vien nhiet doi" should be responded with [{"class": "stop", "keywordorname": ["benh vien nhiet doi"], "attributes": ["_name"], "condition": "fuzzy_compare(a[0], \'benh vien nhiet doi\') == True"}], when dealing with "district" please use "quan", and the attributes shoule be "_zone", for example "district 5" should be "quan 5", when dealing with ward the string when compare should have "phuong" with the number for example "ward 3" should "phuong 3", when the message is required to under condition of two different classes, please use please put the class and its belonging atrributes in another json object, for example find me stop with name benh vien nhiet doi in the route 5 should be responded with [{"class": "stop", "keywordorname": ["benh vien nhiet doi"], "attributes": ["_name"], "condition": "fuzzy_compare(a[0], \'benh vien nhiet doi\') == True"}, {"class": "routeVar", "keywordorname": ["5"], "attributes": ["_routeNo"], "condition": "a[0] == 5"}]. ',
            messages=[
                {"role": "user", "content": messages},
            ]
        )

        print(f"responded!!")

        return message.content[0].text

# bot = respondHandler()
# s = bot.respond("benh vien")

# print(s)