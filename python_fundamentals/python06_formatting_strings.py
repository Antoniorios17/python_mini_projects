#Formatting Strings using the format() method

#The sysntax is:
#"String to be formatted".format(values or variables to be inserted into string, separated by commas)

#We use braces {} like this :
message = '''The price of this {0:s} laptop is {1:d} USD and the
             exchange rate is {2:4.2f} USD to 1 EUR'''.format('Apple', 1299, 1.235235245)

#Inside the braces, we first write the position of the argument to use, followed by a color.
#After the colon, we write the formatter. There should no be any spaces within the braces.

#When we write format('Apple, 1299, 1.235235')
#we are passing in three arguments to the format() method.

#The argument "Apple" has a position 0.
#1299 has a position
#1.235235245 has a position of 2

#position always start at ZERO

#The format() method can be kind of confusing. To get a better understanding of the format() method, try the following program

message1 = '{0} is easier than {1}'.format('Python', 'Java')
message2 = '{1} is easier than {0}'.format('Python', 'Java')
message3 = '{:10.2f} and {:d}'.format(1.23123123, 12)
message4 = '{}'.format(1.232324564)

print(message1)
# You'll get:
#'Python is easier than Java'

print(message2)
#You'll get:
#'Java is easier than Python'

print(message3)
#You'll get:
#'       1.23 and 12'
#You don't need to indicate the positions of the arguments

print(message4)
#You will get:
#'1.232324564' no formatting is done




