import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

data = response.json()

list = 1
print(f"The list of available pokemons is :\n")
for pokemon in data['results']:
    print(f"{list}. {pokemon['name']}")
    list+=1
