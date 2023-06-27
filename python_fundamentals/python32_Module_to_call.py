
# this function will be called on the pytho32 lesson on modules
# This function checks if a number is a prime number

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
    return True