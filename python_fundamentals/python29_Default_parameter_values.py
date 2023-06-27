# default parameter values
# 

def my_function(a, b, c=1, d=2, e=3):
    print(a, b, c, d, e)

# default values can only be assigned to the last parameters 
# in this case c, d, and e
# you cannot assign default parameter values in the middle

#examples
#when call the function
my_function(10, 20)
# we get
# 10 20 1 2 3 because we have default values for the last 3 parameters
# and we assigned values for the first two

my_function(10, 20, 30, 40)
# we'll get
# 10 20 30 40 3 because we assigned values for the first 4 and get default last value


