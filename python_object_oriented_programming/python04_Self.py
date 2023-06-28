# Self
# first we need to discuss the concept of class and instance variables

# a class variable belongs to the class and is shared by all instances of that class
# it is defined outside any method in the class

# an instance variable, on the other hand, is defined inside a method and belongs to the instance
# it is always with the self keyword

#Example

class Prog_staff:
    company_name = "Programming Lab"

    def __init__(self, p_salary):
        self.salary =p_salary

    def print_info(self):
        print("Company name is", Prog_staff.company_name)
        print("Salary is", self.salary)
peter = Prog_staff(2500)
john = Prog_staff(2500)

# we define class called Prog_staff
# this class has a variable called company_name that is not defined anywhere


# now let's explore the difference between class and instance variable
# the name of the company is ProgrammingLab, suppose the names changes to 'Programming School'

Prog_staff.company_name = 'Programming School'

# Notice that we used Prog_staff before company name
# This change will affect ALL INSTANCES of the Prog_staff class

#to verify:
print(peter.company_name)
print(john.company_name)
# you get:
# Programming School
# Programming School
# 
# this is updated company_name


# suppose the Salary of Peter was increase to 2700
# you update it as follows:
peter.salary = 2700

#the only one affected by this change is Peter
print(peter.salary)
print(john.salary)

# you will get
# 2700
# 2500

# SUMMARY

# CLASS VARIABLE
# - A class variable is defined outside any method in the class
# - It can be accessed outside the class using the class name
# - Changing iT affects all instances of the class

# INSTANCE VARIABLE
# - An instance is defined inside a method in the class and prefixed witht the self keyword
# - It can be accessed otuside the class using the name of the instance
# - Changing it only affects the specific instance

# In the example, company_name is a class variable while salary is and instance variable


#to call the print_info method we type
peter.print_info()
# we get:
# Company name is Programming School
# Salary is 2700

# python calls to the self parameter implicitely for us
# we don't have to do it ourselves

# Alternatively we can use the class name:

Prog_staff.print_info(john)
# both ways will return the same response

