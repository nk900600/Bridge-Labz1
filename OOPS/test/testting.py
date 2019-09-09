import json

with open("test") as f:
    data=json.load(f)

for i in range(len(data)):
    for j in data[0].values():
        for k in j.values():
            if k[0]["name"]:
                k[0]["name"].append("manny")
                print(len(k[0]["name"]))
