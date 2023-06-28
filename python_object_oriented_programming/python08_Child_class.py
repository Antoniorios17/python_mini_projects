# child class
# also known as sub class or derived class

# the class from which it is derived is known as a 
# base class, a super class, or a parent class

# the main feature of a sub class is that it inherist all the variables and methods from the parent class.
# it can use the variables and methods of the parent class as its own
# as well as new variables and methods that do not exist in the parent class

# we'll add the line below to python08_sample_class.py:
# class management_staff(staff): 

# we are creating a new class called management_staff(staff)

# also add the __init__ method for the subclass

# one of the main reasons for subclasses is to facilitate code reuse.
# one way to do it is to use a built-in function called 
#               super()

# we added all this code:

# class management_staff(staff):
#     def __init__(self, p_name, p_pay, p_allowance, p_bonus):
#         super().__init__('Manager', p_name, p_pay)
#         self.allowance = p_allowance
#         self.bonus = p_bonus

# Within the method, the first line uses the super() fucntion to call the __init__ method
# in the base class. The super function() is a pre-built function that we can use in a
# a subclass to call a method in the super class

# when we use super() to call a method in the parent class, we do not have to pass 
# in any value for the self parameter.

# in the example, we do not need to pass in three values( the string 'Manager' and the parameters p_name and p_pay )
# to the base class __init__ method. 
# The base class method will be called and the string 'Manager' will be assigned to _position
# while p_name and p_pay will be assigned to name and pay respectively

# Besides using the super() function, we can also use the parent class name
# to call a method in the base class. To do that, we write

# staff.__init__(self, 'Manager', p_name, p_pay)


# After calling the __init__ method in the base class, the sub class __init__ method
# uses the two statement below to asign the parameters p_allowance and p_bonus
# to the instance variables allowance and bonus respectively.

# self.allowance = p_allowance
# self.bonus = p_bonus

# These two instance variables only exist in the subclass
# They do not exist in the super class. That's all fot the __init__ method in the sub class


# Now, let us code a method to calculate the pay of a management staff.
# add the following method to management_staff

#  def calculate_pay(self):
#         basic_pay = super().calculate_pay()
#         self.pay = basic_pay + self.allowance
#         return self.pay

# Notice that this method uses the super() fucntion again to call the calculate_pay()
# method in the base class. After calling the base class method, we assign the result to the variable basic_pay
# is a local variable that only exists within the calculated_pay() method.
# Hence, you do no need to prefixit with the keyword self.

# Next, we add the value of basic_pay to the instance variable allowance to calculate the total pay
#  of the management staff. We then assign it to the instance variable pay and return this value
#  in the next statement


# Now we are going to add a submethod to the class. Suppose a management staff is also entitled to
#  perfomance bonus if their performance grade is an 'A'.
# to calculate the performance bonus of a management staff
# we can add a new method to the management_staff class:

# def calculate_perf_bonus(self):
#         prompt = 'Enter performance grade for %s: ' %(self.name)
#         grade = input(prompt)
#         if (grade == 'A'):
#             self.bonus = 1000
#         else:
#             self.bonus = 0
#         return self.bonus

# This method first asks the user to enter performance grade for the management staff
# it then assigns either 1000 or 0 to the instance variable bonus based on the performance
# entered. Finally, returns the value of bonus in the next statement

# Before we end this section, we shall dervice one more sub class from staff.
# this time the derived class is called basic_staff
# the code is shown below:

# class basic_staff(staff):
#     def __init__(self, p_name, p_pay):
#         super().__init__('Basic', p_name, p_pay)


# This sub class only overrides the __init__ method in the base class. The __init__
# method passes in the string 'Basic' to the base class initializer so that the 
# instancevariable_position will be assigned automatically when we instantiate a 
# basic_staff object. Other than that, the sub class inherits allother variables
# and methods from the base class. The class has the following content



