import json
filename = "readfromjson.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)
#print (jsonobject)
for employee in jsonobject["employees"]:
    print(employee["firstName"])