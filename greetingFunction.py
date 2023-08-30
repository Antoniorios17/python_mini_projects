def greeting(input):
    output = f'Hello {input}!'
    return output

# print(greeting("antonio"))

print("Welcome to the greeting program: ")

while True:
    user_input = input('''Please enter your name or type exit to leave: 
                          Or type exit to leave \n''')
    if user_input == "exit":
        break
    else:
        print(greeting(user_input))
        response = input("Would you like to continue")
        if response[0].split().lower() == "y":
            continue
        else:
            break


