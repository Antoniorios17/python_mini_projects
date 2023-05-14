import json
import requests
from random import randint

#This scrypt will allow the user to type down a food item and the program will return a drink a goes well with it
#The input from the user can only be a string
#the users can select any food choice as a string

food_choice = input('Please enter your dinner choice: ')

#the link to the API is stored in the variable url to be used later
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

# r is the new rariable containing the contents of the API
r = requests.get(url)

data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': abv
                 }
    beer_list.append(beer_item)

value = randint(0, len(beer_list))

try_this = beer_list[value]

try_name = try_this['name']
try_tagline = try_this['tagline']
try_abv = try_this['abv']

print(f'You should try {try_name}, {try_tagline}, {try_abv}pie %')
