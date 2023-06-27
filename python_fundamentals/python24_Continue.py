#Continue

# Continue is very useful with loops
# 
j = 0
for i in range(5):
    j = j + 2 
    print('\ni = ', i, ', j = ',j )
    if j ==6:
        continue
    print('I will be skipped over if j = 6')

# you will get 
# i =  0 , j =  2
# I will be skipped over if j = 6

# i =  1 , j =  4
# I will be skipped over if j = 6

# i =  2 , j =  6

# i =  3 , j =  8
# I will be skipped over if j = 6

# i =  4 , j =  10
# I will be skipped over if j = 6

