import anthropic
import dotenv
import os

class respondHandler():
    def __init__(self):
        self.stopData = "<className>stop</className> has these attributes: <listAttributes>'_stopId', '_code', '_name', '_stopType', '_zone', '_ward', '_addressNo', '_street', '_supportDisability', '_status', '_lng', '_lat', '_search', '_routes'</listAttributes>"
        self.routeVarData = "<className>routeVar</className> has these attributes: <listAttributes>'_routeId', '_routeVarId','_routeVarName','_routeVarShortName','_routeNo','_startStop','_endStop','_distance','_outBound','_runningTime'</listAttributes>"

        self.cmpFunc = "<funcAndUsage>fuzzy_compare(string, string): use when compare string, compare the similarity of two strings a and b, return True if the similarity is greater than or equal to 80, otherwise return False.</funcAndUsage>"

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
            system = f"given the data [{self.routeVarData}, {self.stopData}], and funtions list {self.cmpFunc} return the class, the list of attribute named 'attributes' that are used in condition and the condition string that python can understand, the i-th attribute in the 'attributes' should be a[i] in the condition string, with 'i' is the index of that attribute in the 'attributes', starting from 0, respond only in json format in one line.",
            messages=[
                {"role": "user", "content": messages},
            ]
        )

        print(f"responded!!")

        return message.content[0].text

# bot = respondHandler()
# s = bot.respond("find me stop name 'benh vien' and support disable while having id greater than 100 ")

# print(s)