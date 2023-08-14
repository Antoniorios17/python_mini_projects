import hashlib

print("=================================")
print("Welcome to the Encryption Creator")
print("=================================\n\n")
secret_message = 'Is is a super secret message'

bsecret_message = secret_message.encode()

# Creates Hashed Object
m = hashlib.md5()


m.update(bsecret_message)

print(m.digest())

user_input = input("Please enter your message")

