import json
f = open("../data/vars.json", "r", encoding="utf-8")


for line in f.readlines():
    tmp = json.loads(line)
    print(len(tmp), end = ' ')

f.close()