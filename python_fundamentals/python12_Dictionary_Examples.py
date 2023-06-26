# run the following program to see this in action

#declaring the dictionary
my_dict = {"one": 1.35, 2.5:"two point five", 3:"+", 7.9:2}

#print the entire dictionary
print(my_dict)

#you'll get {"one": 1.35, 2.5:"two point five", 3:"+", 7.9:2}

#print the item with key "one"
print(my_dict["one"])
#you'll get 1.35

#print the item with key 7.9
print(my_dict[7.9])
#you will get 2

#modify the item with key = 2.5  and print the updated dictionary
my_dict[2.5] = "two and a half"
print(my_dict)

#add a new item and print the updated dictionary
my_dict["New item"] = "I'm new"
print(my_dict)
#you will get {'one': 1.35, 2.5: 'two and a half', 3: '+', 7.9: 2, 'New item': "I'm new"}

#remove the item with the key = "one" and print the updated dictionary
del my_dict["one"]
print(my_dict)
#you'll get {2.5: 'two and a half', 3: '+', 7.9: 2, 'New item': "I'm new"}






