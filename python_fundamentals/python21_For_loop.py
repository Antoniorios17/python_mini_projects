#for loop

# executes a block of code repeatedly until the condition in the for statement is no longer valid
#syntax

# for a in iterable:
#     print(a)

# Example
 
# pets = ["cats", "dogs", "rabbits", "hamsters"]

# for mypets in pets:
#     print(mypets)

# #if you run the program you will get
# # cats
# # dogs
# # rabbits
# # hamsters

# # we can also display the index of the members in the list.
# #to do that we use the enumerate() Function

# for index, mypets in enumerate(pets):
#     print(index, mypets)

#to loop over dictionary

#example
# age = {"Peter":5, "John":7}

# for i in age:
#     print(i)
# #you'll get 
# Peter
# John

#if we want the key and value
#we can do it this way

#Example

# age = {"Peter":5, "John":7}

# for i in age:
#     print("Name = %s, Age = %d" %(i, age[i]))
# when you run the program you will get
# Name = Peter, Age = 5
# Name = John, Age = 7  


#alternatively you can use the items() method
# age = {"Peter":5, "John":7}

# for i, j in age.items():
#     print("Name = %s, Age = %d " %(i, j))
#you will get
# Name = Peter , Age = 5 
# Name = John , Age = 7 


#loop through a string

# message = "Hello"
# for i in message:
#     print(i)
#you'll get
# H
# e
# l
# l
# o


# looping through a sequence of numbers:
# use the built-in range() function
# syntax
# ranged(start, end, step)
# starts at zero by default

# range(5) will generate the list [0, 1, 2, 3, 4]
# range(3,10) will generate the list [3, 4, 5, 6, 7, 8, 9]
# range(4, 10, 2) will generate the list  [4, 6, 8]

for i in range(5):
    print(i)

# you will get 
# 0
# 1
# 2
# 3
# 4

