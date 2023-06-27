# Creating your own module

#You can create your own module to use in other projects
# I placed the checkifprime() function in python32_Module_to_call.py
# we will import that function by calling the module
import python32_Module_to_call as prime
# we are also adjusting the name of the module to prime as the new alias
answer = prime.checkIfPrime(13)
print(answer)

# you will get 
# True