# Opening and reading text files by buffer size

# We can read a file by buffer size using read() instead of readline()
# so that we decrease the memory usage of the program
# we can also specify the buffer size we want 

# example

input_file = open('python33_text_sample_file.txt', 'r')
output_file = open('python36_output_file.txt', 'w')

msg = input_file.read(10)

# print(len(msg))
while len(msg):
    output_file.write(msg + '\n')
    msg = input_file.read(10)

input_file.close()
output_file.close()

#this code will create another file that will have the same content as the initial file
# the difference being that the output file will be written in segments of 10 bytes every time
# while the condition is true

# this is what you get
# each line represents 10 bytes of data being transfered to the new file 
# as it's being read

# This is th
# e first li
# ne
# This is
#  the secon
# d line
# Pyt
# hon for Be
# ginners
# He
# llo World

# google.com

# This sent
# ence will 
# be appende
# d
# Python i
# s fun

