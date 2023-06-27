# Using a for loop to read text files
# readline() can be helpful to read files
# we can also use a for loop to read files
# 
# The following program shows how it's done
f = open('python33_text_sample_file.txt', 'r')
for line in f:
    print(line, end ='')
f.close()

#the for loop goes line by line reading the file.
# you will get 
# This is the first line
# This is the second line
# Python for Beginners
# Hello World
# google.com

