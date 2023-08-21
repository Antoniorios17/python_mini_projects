import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

data = response.json()

list = 1
for pokemon in data['results']:
    print(list, pokemon['name'])
    list+=1
