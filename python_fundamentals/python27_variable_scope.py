# Variable Scope

# variable defined inside a function are not the same as outside
# any variable that is declared inside a function is only accessible within the function
# these are known as local variables
# any variable declared outside the function is known as a global variable
# and it is accessible anywhere in the program

# example

# message1 = "Global variable"

# def my_function():
#     print("\nINSIDE THE FUNCTION")
#     #Global variables are accessible inside a function
#     print(message1) 
#     #declaring a local variable
#     message2 = "local variable"
#     print(message2)

# '''
# Calling the function
# Note that my_function() has no parameters.
# Hence, when we call this function,
# we use a par of empty parentheses.
# '''

# my_function()
# print("\nOUTSIDE THE FUNCTION")
# #global variables are accessible outside function
# print(message1)
# #local variables are NOT accessible outside the function
# print(message2)

# you will get
#INSIDE THE FUNCTION
# Global variable
# local variable

# OUTSIDE THE FUNCTION
# Global variable
# Traceback (most recent call last):
#   File "python27_variable_scope.py", line 33, in <module>
#     print(message2)
# NameError: name 'message2' is not defined



#Another concept to understand is when a local variable shares the same name with a global variable
# any code inside the function is accessing the local variable
# any code outside the function is accessing the global variable
#example

message1 = "Global Variable" #(Shares same name as a local variable)
def my_function2():
    message1 = "local variable" #Shares same name as the global variable
    print('INSIDE THE FUNCTION')
    print(message1)

#calling the function
my_function2()

#printing message1 OUTSIDE the function
print('\nOUTSIDE THE FUNCTION')
print(message1)

#you will get this output
# INSIDE THE FUNCTION
# local variable

# OUTSIDE THE FUNCTION
# Global Variable


