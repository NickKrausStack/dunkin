import requests
import json

url = 'https://www.dunkindonuts.com/bin/servlet/dsl'
response = requests.post(url, allow_redirects=False, data={
    'service': "DSL",
    'origin': '37.7749, -122.4194',
    'radius': "100000",
    'maxMatches': "100000"
})

content = json.loads(response.content)
newJson = {"data": []}

for entry in content["data"]["storeAttributes"]:
    entry["geoJson"] = json.loads(entry["geoJson"])
    newJson["data"].append(entry)

with open('dunkinDonuts.json', 'w') as jsonFile:
    json.dump(newJson, jsonFile)
