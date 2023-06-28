# Importing a class

# We are going to import the classes on the file
# python06_sample_class.py

import python06_sample_class

sc = python06_sample_class.some_class()
sc.some_method(100)

soc = python06_sample_class.some_other_class()
# you will get:
# 
# This is some_class
# The value of a is  100
# This is some_other_class

# in the code above, we instantiated the objects by prefixing the class name with the file name
# such as python06_sample_class.some_class() so that the compiler knows that some_class()
# is in the file python06_sample_class.py


# Another way to do it would be:
from python06_sample_class import some_class, some_other_class

# if you do it this way you don't need to prefix the file name when instantiating an object
# example:

sc = some_class()
soc = some_other_class()

# you will get:
# This is some_class
# This is some_other_class
