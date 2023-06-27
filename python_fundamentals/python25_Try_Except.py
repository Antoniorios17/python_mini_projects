# Try, Except

# The final control statement is try, except.
# this statement controls how the program proceeds when an error occurs
# syntax

# try:
#     do something
# except:
#     do something else when an error occurs


#example
# try:
#     answer = 12/0
#     print(answer)
# except:
#     print("An error occurred")


# Example
# specific error messages
try:
    user_input1 = int(input("Please enter a number: "))
    user_input2 = int(input("Please enter another number: "))
    answer = user_input1 / user_input2
    print("The answer is ", answer)
    my_file = open("missing.txt", 'r')
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown error", e)



#other common errors in python 

# IOError
# Raised when an I/O operation (such as the built-in open() function)fails
# for I/O related reason,such as  "file not found"

# ImportError
# Raise when an import statement fails to find the module definition.


# IndexError
# Raised when a sequence(string, list, tuple) index is out of range

#KeyError
#Raised when a dictionary Key is not found

#NameError:
# Raised when a local or global name is not found

#TypeError
# Raised when an operation or function is applied to an object of inappropiate type



