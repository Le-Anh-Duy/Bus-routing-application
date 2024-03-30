import anthropic
import dotenv
import os

dotenv.load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(
    api_key=anthropic_api_key,
)

pathData = "<className>path</className> has these attributes: <listAttributes>_lat, _lng, _routeId, _routeVarId</listAttributes>"

routeVarData = "<className>routeVar</className> has these attributes: <listAttributes>'_routeId', '_routeVarId','_routeVarName','_routeVarShortName','_routeNo','_startStop','_endStop','_distance','_outBound','_runningTime'</listAttributes>"

stopData = "<className>stop</className> has these attributes: <listAttributes>'_stopId', '_code', '_name', '_stopType', '_zone', '_ward', '_addressNo', '_street', '_supportDisability', '_status', '_lng', '_lat', '_search', '_routes'</listAttributes>"

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system = f"given the data [{pathData}, {routeVarData}, {stopData}], return the class, the list of attribute use in condition and condition string that python understand, Respond only in json format in one line.",
    messages=[
        {"role": "user", "content": "find me a route variations that passes through stop 1 and stop 2."},
    ]
)

print(message.content)