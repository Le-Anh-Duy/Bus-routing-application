import anthropic
import dotenv
import os

class respondHandler():
    def __init__(self):
        self.stopData = "<className>stop</className> has these attributes: <listAttributes>'_stopId', '_code', '_name', '_stopType', '_zone', '_ward', '_addressNo', '_street', '_supportDisability', '_status', '_lng', '_lat', '_search', '_routes'</listAttributes>"
        self.routeVarData = "<className>routeVar</className> has these attributes: <listAttributes>'_routeId', '_routeVarId','_routeVarName','_routeVarShortName','_routeNo','_startStop','_endStop','_distance','_outBound','_runningTime'</listAttributes>"
        self.pathData = "<className>path</className> has these attributes: <listAttributes>_lat, _lng, _routeId, _routeVarId</listAttributes>"

        dotenv.load_dotenv()
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(
            api_key=anthropic_api_key,
        )

    def respond(self, messages):

        print(f"responding, please wait...")

        message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            system = f"given the data [{self.pathData}, {self.routeVarData}, {self.stopData}], return the class, the list of attribute use in condition and condition string that python understand, each attribute in the condition should be 'a[i]', with 'i' is the index in the returned atrributes list, respond only in json format in one line.",
            messages=[
                {"role": "user", "content": messages},
            ]
        )

        print(f"responded!!")

        return message.content[0].text

# bot = respondHandler()
# s = bot.respond("find me a route variations that has running time less than 10 minutes and distance less than 5 km.")

# print(s)