import json

with open("state_city_json") as f:
    country=json.load(f)
cities=[]
for i in range(len(country)):
    for j in country[i]["maharastra"].values():
        cities.append(j)
for i in range(len(country)):
    for j in country[i]["gujrat"].values():
        cities.append(j)
for i in range(len(country)):
    for j in country[i]["punjab"].values():
        cities.append(j)
