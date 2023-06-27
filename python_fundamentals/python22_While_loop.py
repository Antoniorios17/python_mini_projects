#while loop

# repeatedly executes instructions inside the loop while a certain condition remains valid.
#syntax
# while a condition is true:
#   do A

# While loops require a variable as a counter
# The condition in the while statement will evaluate the value fo counter to determine
# if it's greater or smaller than a certain value

#example

counter = 5

while counter > 0:
    print("Counter = ", counter)
    counter = counter -1
# you will get
# Counter =  5
# Counter =  4
# Counter =  3
# Counter =  2
# Counter =  1


# we need to decrease the value of the counter to prevent infinite loops
# The condition needs to eventually become false
