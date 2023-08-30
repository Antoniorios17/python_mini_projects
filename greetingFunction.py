def greeting(input):
    global name
    name = input.capitalize()
    output = f'Hello {name}!'
    return output

# print(greeting("antonio"))

print("Welcome to the greeting program:\n ")

while True:
    user_input = input('Please enter your name: \nOr type exit to leave: \n')
    if user_input == "exit":
        break
    else:
        print(greeting(user_input))
        response = input("Would you like to continue {} ? ".format(name))
        if response[0].lower() == "y":
            continue
        else:
            break


