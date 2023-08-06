print("welcome to fruit selector")
entry = input("Select the first letter of your fruit: ")

fruits = ["apple", "orange", "pineapple"]
veggies = ["onion", "potato", "carrot"]

for fruit in fruits:
    if fruit[0] == entry:
        print(f'The fruit that start with {entry} is {fruit}')


