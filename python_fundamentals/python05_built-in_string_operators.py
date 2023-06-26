#Built-in String Functions
#Python Includes functions to manipulate strings

#upper() capitalizes all letters in a string
#"peter".upper() = "PETER"

#Formating Strings using the % Operator
#The syntax for using the operator is 

#"string to be formatted" %(values or variables to be inserted into string, separated by commas)

brand = "Apple"
exchangeRate = 1.23
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)

print(message)

#%s, %d and 4.2f are known as formatters; They serve as placeholders in the string
#They will be replaced with brand, the value 1299 and exchangeRate

#Output

#The price of this Apple laptop is 1299 and the exchange rate is 1.24 USD ot 1 EUR

#The %s formatter is used to represent a string


#The %d formatter represents an integer
#If we want to add spaces before an integer, we can add a number between a % and d to indicate the desired lenght of the string
#Example
#"%5d" will give us "  123" with 2 space in front and a total lenght of 5


#The %f formatter represents a float
#Here we format it as %4.2f where 4 refers to the total lenght and 2 refers to 2 decimal places
#If we want to add spaces before the number, we can format it as %7.2f
#which will give us "    1.24" with 2 decimal places and 3 spaces in front and a total lenght of 7







