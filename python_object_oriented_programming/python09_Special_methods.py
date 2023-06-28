# Python Special Methods

# two of the magic methods used are __init__ and __str__

# Another property of special methods is that they can overriden to suit
# our needs. The __str__ method is commonly overriden to provide a more human
# readable string representation of a class

# other methods that commonly overridenare the 
# __add__, __sub__, __mul__, __div__ methods.
# these methods allows us to modify standard operator such as the +, -, * and /
# so that they can do different things depending on what they are operating on.

# The + operator add the two numbers 
# Example
# 2 + 3 = 5
# also 
# 'Hello' + " World"  -->  "Hello World"
# + sign contatenates the two strings to return "Hello World"

# There is a special method for every operator sign
# we can override them to provide more meaning to them
#This is known as overloading

# These two lines will be added to python08_sample_class.py

# def __add__(self, other):
# return self.pay + other.pay

# This method overrides the __add__ method. It has two parameter self and other.
# 
# Self refers to one instance, other refers to another instance.
# it basically tells the compiler to add the pay variable of both instances and return the result

# to call the method, we use the + operator

# add the following lines

import python08_sample_class

peter = python08_sample_class.basic_staff('Peter', 0)
john = python08_sample_class.management_staff('John', 0, 1000, 0)

print(peter)
print(john)

print('Peter\'s pay = ' , peter.calculate_pay())

print('John\' Pay = ', john.calculate_pay())
print('John\'s Performance Bonus = ', john.calculate_perf_bonus())

total_pay = john + peter
print('\n Total Pay for both staff = ', total_pay)


# Run the proragm and key in
# 120, 15,150, 20 and A when prompted.

# you will get 
# total pay for both staff = 5800

# the full answer is below

# Creating Staff object
# Creating Staff object
# Position = Basic, Name = Peter, Pay = 0
# Position = Manager, Name = John, Pay = 0

# Enter number of hours worked for Peter: 120
# Enter hourly rate for Peter: 15
# Peter's pay =  1800

# Enter number of hours worked for John: 150
# Enter hourly rate for John: 20
# John' Pay =  4000
# Enter performance grade for John: A
# John's Performance Bonus =  1000

#  Total Pay for both staff =  5800