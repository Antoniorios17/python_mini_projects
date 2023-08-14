import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

data = response.json()

# print(data.keys())
print(data['results'][0])
for pokemon in data['results']:
    print(pokemon)