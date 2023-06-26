#Dictionary

#Dictionary is a collection of related data pairs
#to declare a dictionary , you write:
# dictionary_name = {dictionary key: data}
# keys must be unique within the dictionary

# Example:

user_name_and_age = {"Peter": 38, "John":51, "Alex":13, "Alvin":"Not Available" }

# You can also declare a dictionary using the dict() method
# To declare the dictionary above, you write:

user_name_and_age = dict(Peter = 38, John = 51, Alex =13, Alvin = "Not available")

# to access the individual items in the dictionary, we use dictionary keys,
# which is the first value in the {dictionary key : data} pair.

# to get Johns age, you write :
# 
user_name_and_age["John"] # you will get value 51

#Modify pairs

# to modify the pair "john": 51 , we write:
user_name_and_age["John"] = 21
# the dictionary updates to:
# user_name_and_age = {"Peter": 38, "John":21, "Alex":13, "Alvin":"Not Available"}


#Empty Dictionary

# we can also declare a new dictionary without any values to it.
dictionary_name = {}


# Add items

# to add items to the empty dictionary , we write:
# dictionary_name[dictionary key] = data
# if we want to add "Joe":40

user_name_and_age["Joe"] = 40

# Our dictionary now becomes:
#user_name_and_age = {"Peter": 38, "John":21, "Alex":13, "Alvin":'Not available', 'joe': 40}

#remove items

#to remove items we write:
#del dictionary_name[dictionary key]
#example:
#del user_name_and_age["Alex"]
user_name_and_age = {"Peter":38, "John":21, "Alvin": "Not Available", "Joe": 40}





