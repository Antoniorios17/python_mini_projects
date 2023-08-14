import hashlib

print("=================================")
print("Welcome to the Encryption Machine")
print("=================================\n\n")



def encryptor(message):
    new_message = message.encode()
    #creates a hash object
    m= hashlib.md5()
    encryption = m.update(new_message)
    return encryption




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

