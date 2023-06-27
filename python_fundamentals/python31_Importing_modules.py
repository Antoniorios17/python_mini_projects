# Importing modules
# to use the built-in code in python modules we have to import them first
# we do that using "import"

#example
import random
#to use randrange() function in the random module
#we write:
random.randrange(1,10)

#if you find it troublesome to write random each time
# import random as r
# where r will act as an alias for random
#now you can write the same function like this:
import random as r
r.randrange(1,10)

# you can also import specific functions from the modules
# from module import name1[, name2[, ...nameN]]

#to import only randrange
from random import randrange
#for multiple functions
from random import randrange, randint

#we don't need the dot notation anymore
# we can simply type:
randrange(1,10)

