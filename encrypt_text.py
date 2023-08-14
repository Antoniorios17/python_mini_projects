import hashlib

print("=================================")
print("Welcome to the Encryption Machine")
print("=================================\n\n")



def encryptor(message):
    #creates a hash object
    encryption = hashlib.md5(message.encode())
    new_message = print(f"The String \"{message}\" is equal to the hash {encryption}")
    return new_message




while True:
    user_input = input("Please enter your message: ")
    if user_input != 0:
        print(encryptor(user_input))
    else:
        print("Not a Valid input")
        new_try = input("Would you like to try again?: (yes/no)")
        if new_try == 'y':
            continue
        else:
            print("")
            print("Thank you, Goodbye")
            print("")

