# Python Built-in Functions for Objects

#two explore the built-in functions consider the code below

class parent_class():
    def __init__(self):
        self.a =1
        print("Parent class object created")
    def some_method(self):
        print('Hello')

class child_class(parent_class):
    def __init__(self):
        print('Child class object created')

parent = parent_class()
child = child_class()


# Example
print("isinstance()")
# isinstance() takes two arguments. it checks if the first argument is an instance of the second argument
print(isinstance(parent, parent_class))
#you get 
# True

# Example2
print(isinstance(5, int))
# you get:
# True
# Because int is a built-in type in python for integers

#example3
print(isinstance(child, parent_class))
# you get
# True
# child is an instance of child_class, which is a subclass of parent_class

# example4
print(isinstance(parent, (parent_class ,int )))
# you get
# True
# parent is an instance of parent_class, which is one of the types in the tuple(parent_class, int)


# issubclass
# this function takes in two arguments 
# it checks if the first argument is a subclass of the second argument

#example
print("\nissubclass()")
print(issubclass(child_class, parent_class))
print(issubclass(parent_class, parent_class))
print(issubclass(child_class, int))
print(issubclass(child_class, (int, parent_class)))



# hasttr()

# this function test if an instance has a certain attribute.
# an attribute can refer to both data(variables) and methods.
# it takes two arguments

print("\nhasttr()")
print(hasattr(parent, 'a'))
print(hasattr(parent, 'some_method'))
print(hasattr(parent, 'b'))