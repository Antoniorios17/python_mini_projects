print("welcome to fruit selector")

entry = input("Select the first letter of your fruit: ")

fruits = ["apple", "orange", "pineapple"]

def fruit_select(entry):
    for fruit in fruits:
        if fruit[0] == entry:
            response = f'The fruit that start with {entry} is {fruit}'
        return response


print(fruit_select(entry))