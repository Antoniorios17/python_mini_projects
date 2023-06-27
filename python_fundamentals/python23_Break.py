#Break

# When working with loops you may want to exit the loop, when a certain condition is met
# to do that, we use the break keyword

#example
j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ',j )
    if j == 6:
        break 
# you will get 
# i =  0 , j =  2
# i =  1 , j =  4
# i =  2 , j =  6

# without the break i would go from 1 to 4
# break stops the loop when j reaches 6

