#Lists
#Collection of data which are normally related

#to declare a list, you write list_name = [initial values]
#We used squared brackets when declaring a list.
#Multiple values are separated by a comma

#Example:
user_age = [21, 22, 23, 24, 25]

#We can also declared a list without any initial values:
#Example:
sample_list = []
#what we have now is an empty list without any values in it
#we have to use append() method to add items to the list.

#Individual values in the list are accesible by their indexes, always starting at ZERO, not 1.
#Example:

fruit_list = ["apple", "cherry"]
#fruit_list[0] correspond to "apple"
fruit_list[0]
#fruit_list[1] correspond to "cherry"
fruit_list[1]

#Alternatively you can access values of a list from the back.
#the last item on the list is -1, the second last has an index of -2
fruit_list[-1]
#will return "cherry"
fruit_list[-2]
#will return "apple"

#You can assign a list or part of it to a variable. if you write
user_age2 = user_age
#The variable user_age2 = becomes [21, 22, 23, 24, 25]

#if you write
user_age3 = user_age[2:4]
#you are assigning items which index 2 to index 4 from the list user_age to user_age3 
#which means 
#user_age3 = [23, 24]

#The notation 2:4 is known as a slice. Whenever we use the slice notation in python.
#The start index is always included while the index at the end is excluded.
#Hence the notation 2:4 refers to items from index 2 to index 4-1(index 3)
#which is why is users_age3 = [23, 24]

#The slice notation includes a third number known as the stepper.
#if we write user_age[1:5:2]
#we will get a sub list consisting of every second number from index 1 to 5-1 because the stepper is 2.

#Slicing notation have useful defaults:
user_age[:4]
#will give you values from index 0 to 4-1
user_age[1:]
#will give you values from index 1 to 5-1 because the size of the list is 5, userage has 5 items

#Modifying lists

#to modify a list write:
#list_name =[index of imtea to be modified] = new value
# example
# if you want to modify the second item, from userage
# user_age[2] = 5
# Your list becomes user_age = [21, 5, 23, 24, 25]


# Add items

# You use the append() function.
# if you write user_age.append(99), you add the value 99 to the end of the list.
# your list is now user_age = [21, 5, 23, 24, 25, 99]


# Remove Items from list

#your write:
# del list_name[index of item to be deleted]
#if you write:
#del user_age[2]
#your list now becomes user_age = [21, 5, 24, 25, 99] (the third item is delete)


