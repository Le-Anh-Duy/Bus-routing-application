import anthropic
import dotenv
import os

dotenv.load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
print(anthropic_api_key)
client = anthropic.Anthropic(
    api_key=anthropic_api_key,
)

pathData = "<className>path</className> has these attributes: <listAttributes>_lat, _lng, _routeId, _routeVarId</listAttributes>"

routeVarData = "<className>routeVar</className> has these attributes: <listAttributes>'_routeId', '_routeVarId','_routeVarName','_routeVarShortName','_routeNo','_startStop','_endStop','_distance','_outBound','_runningTime'</listAttributes>"

stopData = "<className>stop</className> has these attributes: <listAttributes>'_stopId', '_code', '_name', '_stopType', '_zone', '_ward', '_addressNo', '_street', '_supportDisability', '_status', '_lng', '_lat', '_search', '_routes'</listAttributes>"

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0.0,
    system = f"extract all the name or keyword in the message, and put it in a list of string, for example, when the message is 'what is quan 5 in vietnamese', the list of string should be ['quan 5', 'vietnamese']",
    messages=[
        {"role": "user", "content": "what is quan 5 in vietnamese"},
    ]
)

print(message.content)