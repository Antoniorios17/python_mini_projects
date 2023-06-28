# Class and Static Methods

# in addition to instant methods python also has 
#       Class
#  and, Static methods:

# Example

class Method_demo:
    a = 1
    @classmethod
    def classM(cls):
        print('Class Method. cls.a = ', cls.a)

    @staticmethod
    def staticM():
        print('Static method')
    
# this class has class variable a and two methods
    # classM()  and,
    # staticM()

# the first method classM(), is a class method
# a class method has a class object(instead of self) as the first parameter
#         cls  is commonly used to represent that class object

# cls is sort of similar to self. 
# the main difference is self refers to an instance while cls refers to a class.
# cls refers to the class itself, we can use it to access our class variables

# Example:
Method_demo.classM()
# we'll get
# Class Method. cls.a =  1

# alternatively we can instantiate a Method_demo object and use it to call the method as shown:

md1 = Method_demo()
md1.classM()
# we'll get
# Class Method. cls.a =  1



# Python has also static methods
# Static methods don't have passed an instance or a class.
# it does not have self or cls as the first parameter.
# Exmaple

md1.staticM()
# OR
Method_demo.staticM()
#we'll get
# Static method
# Static method

# Class and static methods are not very commonly used.
# In most cases, instance methods are all that is required in a python class
