import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data{response.status_code}")

pokemon_name = "doduo"

pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info['name'].capitalize()}")
#     print(f"Id: {pokemon_info['id']}")
#     print(f"Height: {pokemon_info['height']} ft")
#     weight_kg = pokemon_info["weight"]*0.45
#     print(f"Weight: {pokemon_info['weight']} lb and {weight_kg} kg")

def get_pokemon_id():
    id = pokemon_info['id']
    return f'Id: {id}'
print(pokemon_name, get_pokemon_id())
    
