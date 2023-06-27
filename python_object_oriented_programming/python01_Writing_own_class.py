# Object oriented programming

# Breaks programming into objects that interact with each other
# Objetcs are created from templates known as classes
# an object is the actual building that we build based on the blueprint

# to Understand how OOP works
# we can write our own class

# we write class followed by the name of the class
# syntax

# class name_of_class
# Example
# This class can be used to store al the relevant information about a staff in the company

class staff:
    def __init__(self, p_position, p_name, p_pay):
        self.position = p_position
        self.name = p_name
        self.pay = p_pay
        print("Creating Staff object")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay)
    
    def calculate_pay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter hourly rate for %s: ' %(self.name)
        hourly_rate = input(prompt)
        self.pay = int(hours)*int(hourly_rate)
        return self.pay

# Instantiating an object

office_staff1 = staff('Basic', 'Yvonne', 0)

# to access the variable name
print(office_staff1.name)

# to accesss the variable position
print(office_staff1.position)

# to change variable position and print it again
# change variable position
office_staff1.position = 'Manager'
print(office_staff1.position)

# to access the variable pay
print(office_staff1.pay)


# METHODS
# to use calculatepay() method
office_staff1.calculate_pay()
print(office_staff1.pay)


# to Print a representation of Office_staff1
print(office_staff1)
# you get
# Position = Manager, Name = Yvonne, Pay = 600