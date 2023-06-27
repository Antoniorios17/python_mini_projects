# Name Mangling

# When you don't want other programmers to change variables directly
# You can add a single underscore in front.

# If you really want to send a strong signal to other programmers not to change variables
# you add two underscores _ _ before variables names

#Example
class A:
    def __init__(self):
        self.__x = 5
        self._y = 6

# the code defines class A
# it has variables __x with double underscore
# and variable _y with a single underscore

# Instantiate a class A object
varA = A()

# now, we can try to access the variables
print(varA._y)
# you will get 6

#however if you type
# print(varA.__x)    ERROR
# you get an error

# This is intended 
# when python sees __ 2 underscores 
# it interprets it as _A__x 
# this is known as Name Mangling

# There is still a way to access __x variable
# if you type

print(varA._A__x) 
#you get 5

# there is no absolute way to restrict access to a variable in python








