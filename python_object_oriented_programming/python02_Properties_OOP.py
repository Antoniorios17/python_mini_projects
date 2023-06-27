# Properties
# adding properties to position
# avoid getting values changed by mistake
# based on the last example 

# Change the line
# self.position = p_position to 
# self._position = p_position

# AND

# Change the line
# return 'Position = %s, Name = %s, Pay = %d' %(self.position, self.name, self.pay)  to
# return 'Position = %s, Name = %s, Pay = %d' %(self._position, self.name, self.pay)



class staff:
    def __init__(self, p_position, p_name, p_pay):
        self._position = p_position
        self.name = p_name
        self.pay = p_pay
        print("Creating Staff object")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)
    
    def calculate_pay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter hourly rate for %s: ' %(self.name)
        hourly_rate = input(prompt)
        self.pay = int(hours)*int(hourly_rate)
        return self.pay
    
    @property
    def position(self):
        print('Getter Method')
        return self._position
    
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')


office_staff1 = staff('Basic', 'Yvonne', 0)

#to access the position of office_staff1 , we write:
print(office_staff1.position)
# output
# Creating Staff object
# Getter Method
# Basic

# we are no longer accessing the variable. Instead we are accessing the getter method of the position property
# Since we get "Getter method" as part of the output

# you can still access the position method as before
print(office_staff1.position)

# Now let's try changing the position of office_staff1 to 'Manager'
office_staff1.position = 'Manager'

#verify the changes were made
print(office_staff1.position)
print(office_staff1)

# if you try to make any changes to the position besides the once allowed 
# you will get and error

office_staff1.position = 'CEO'
# you get
# Position is invalid. No changes made.

