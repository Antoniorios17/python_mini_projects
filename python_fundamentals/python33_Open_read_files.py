# Opening and reading files

# First I created a file called python33_text_sample_file.xtx
# we are going to read this file

f = open('python33_text_sample_file.txt', 'r')

first_line = f.readline()
second_line = f.readline()
print(first_line)
print(second_line)
f.close()

# we'll get
# This is the first line

# This is the second line

#first we have to open the file
# open() function requires two arguments
# first: the file name or file path
# second: is the mode -> it specifies how the file will be used
# There are different modes:
#       -r mode:  for reading only
#       -w mode:  for writing only
#                 if it doesn't exist it will be created
#                 if it exist all the data will be erased
#       -a mode:  for appending
#                 if it doesn't exist it will be created
#                 it the file exist, all the data is added to the end
#       -r+ mode: for both reading and writing   
#
# f.readline() function reads a new line in the file
# whenever f.readline is called it will read the next line
#
# readline() adds a \n by default
# if you want to remove it 
# you write:
# print(firstline , end = '') single quotes no double
