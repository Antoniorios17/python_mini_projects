# Writing to a text file

# We'll use 'a' append mode

f = open('python33_text_sample_file.txt', 'a')
f.write("\nThis sentence will be appended")
f.write('\nPython is fun')
f.close()

# if you wanted to check the file again you can use the previous program to read it
# if you run the program multiple times 
# you will end up appending the same last two lines over and over
# f = open('python33_text_sample_file.txt', 'r')
# for line in f:
#     print(line, end= '')
# f.close()


