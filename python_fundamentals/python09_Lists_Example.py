#To understand better the workings of a list:
#run this program

my_list = [1, 2, 3, 4, 5, "Hello"]

#print the entire list.
print(my_list)
#you'll get [1, 2, 3, 4, 5, "Hello"]

#print the third item (index starts at 0)
print(my_list[2])
#you'll get 3

#print the last item
print(my_list[-1])
#you'll get "Hello"

#assign myu_list (from index 1 to 4) to my_list2 and print my_list2
my_list2 = my_list[1:5]
print(my_list2)
#You will get [2, 3, 4, 5]

#modify the second item in my_list and print the updated list
my_list[1] = 20
print(my_list)
#you will get [1, 20, 3, 4 , 5, "Hello"]

#append a new item to my_list and print the the updated list
my_list.append("How are you")
#You will get [1, 20, 3, 4, 5, "Hello", "How are you"]

#remove the sixth item from my_list and print the update list
del my_list[5]
print(my_list)
#you will get [1, 20, 3, 4, 5, "How are you"]



