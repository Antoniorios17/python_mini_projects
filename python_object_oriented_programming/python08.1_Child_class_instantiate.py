# Instantiating a class object 

import python08_sample_class

peter = python08_sample_class.basic_staff('Peter', 0)
john = python08_sample_class.management_staff('John', 0, 1000, 0)

print(peter)
print(john)

print('Peter\'s pay = ' , peter.calculate_pay())

print('John\' Pay = ', john.calculate_pay())
print('John\'s Performance Bonus = ', john.calculate_perf_bonus())


# # you get using 10 and 10 for both hours and salary for both:


# Creating Staff object
# Creating Staff object
# Position = Basic, Name = Peter, Pay = 0
# Position = Manager, Name = John, Pay = 0

# Enter number of hours worked for Peter: 10
# Enter hourly rate for Peter: 10
# Peter's pay =  100

# Enter number of hours worked for John: 10
# Enter hourly rate for John: 10
# John' Pay =  1100
# Enter performance grade for John: A
# John's Performance Bonus =  1000