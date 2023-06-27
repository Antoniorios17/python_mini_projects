# Variable length argument list
# python allows to pass a variable number of arguments to a function.
# very useful if do not know the number of arguments a function has in advance

#example


# def addnumber(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#     print(sum)

# addnumber(1, 2, 3, 4, 5)

#when we add a single asterisk in front of num, we are telling the compiler that
#num stores a variabl-length argument list that contains several items

#the function then loops through the argument to find the sume of all the numbers and return the answer
#we'll get 15 as the output.
# we can also add more number is we wanted to
# addnumber(1,2,3,4,5,6,7,8)
#we'll get 36

# When using * we can pass in a variable number of arguments to the function
# this is known as non-keyworded variable length list.



# keyworded
# if we wanted to pass a keyworded variable length argument list
# we can double the asterisks

#Example

def print_member_age(**age):
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i,j))


#The double asterisk ** makes it work like a dictionary
# to call the function we write

print_member_age(Peter = 5, John = 7)
# We'll get:
# Name = Peter, Age = 5
# Name = John, Age = 7

