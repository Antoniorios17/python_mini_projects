import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

data = response.json()

list = 1
print(f"The list of available pokemons is in this API is :\n")
for pokemon in data['results']:
    print(f"{list}. {pokemon['name'].upper()}")
    list+=1
    

# other list of pokemons
