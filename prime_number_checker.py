# This function is designed to check if the input is a prime number

print("Welcome to the Prime number checker")
number_to_check = int(input("Please enter a number: "))

def checkifprime(Number_to_check):
    for x in range(2, number_to_check):
        if (number_to_check%x == 0):
            return f"The number {number_to_check} is not a prime number"
    return f'The number {number_to_check} is a prime number'

print(checkifprime(number_to_check))



