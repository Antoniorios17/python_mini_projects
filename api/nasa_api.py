import requests
import json

response = requests.get("http://api.open-notify.org/astros")

# print(response.status_code)
# print(response.json())

# print(type(response.json()))

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
