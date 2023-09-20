print("welcome to The Fruit Selector! ")

entry = input("Select the first letter of your fruit: ")

fruits = ["apple", "orange", "pineapple", "kiwi", "Blueberry", "cherry"]

def fruit_select(entry):
    for fruit in fruits:
        if fruit[0].lower() == entry:
            response = f'The fruit that start with {entry} is {fruit}'
        return response


print(fruit_select(entry))