import json

with open("data.json", "r") as f:
    data = json.load(f)
    for a in data:
        print(a['url'])
    print(len(data))
