# Fetching from this feed: http://data.phishtank.com/data/online-valid.json

import requests
import json
import os

response = requests.get("http://data.phishtank.com/data/online-valid.json")

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    subset = data[:50] # first 50 records
    print(json.dumps(subset, indent=2)) # pretty print as JSON

    with open("data/phish-data.json", "w") as f:
        json.dump(subset, f, indent=2)