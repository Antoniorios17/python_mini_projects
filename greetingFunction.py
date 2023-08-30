def greeting(input):
    output = f'Hello {input}!'
    return output

# print(greeting("antonio"))



while True:
    user_input = input("Please enter your name or type exit to leave: ")
    if user_input == "exit":
        break
    else:
        print(greeting(user_input))
        response = input("Would you like to continue")
        continue

