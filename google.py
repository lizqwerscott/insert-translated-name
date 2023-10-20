import requests
import json
import sys

google_url = sys.argv[1]
input = sys.argv[2]

url = '{}/translate/google'.format(str(google_url))

data = {
    "data": input,
    "dest": "en"
}

result = ""
with requests.post(url, json=data) as response:
    data = response.json()
    if data["code"] == 200:
        result = data["data"]

print(json.dumps({"translation": result[1:-1].strip()}))
