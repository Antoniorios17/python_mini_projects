# Opening, Reading and writing binary files

# Binary files refers to any files that contain non-text 
# such as images, video

# to work with binary files we use 
#     rb or wb mode

# we are going to work with jpg
# file name is python37_Sample_image.jpg

#example

input_file = open('python37_Sample_image.jpg', 'rb')
output_file = open('python37_output_image.jpg','wb')


msg = input_file.read(10)

while len(msg):
    output_file.write(msg)
    msg = input_file.read(10)

input_file.close()
output_file.close()


