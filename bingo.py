import random
from tabulate import tabulate 

# a function that sorts the items contained within each nested list
def sortList():
    for x in range(3):
        mylist[x].sort() 

         #[0,0   0,1   0,2]  [1,0   1,1   1,2]  [2,0  2,1  2,2]
mylist = [[None, None, None],[None, None, None],[None,None,None]]

# Iterate through each instance of the entire list. Check for "None", generate random number, check if number exists, assign number to that instance.
for x in range(3):
    for y in range(3):
      while mylist[x][y] == None:
          num = random.randint(0,90)
          if num not in mylist[0] and num not in mylist[1] and num not in mylist[2]: 
            mylist[x][y] = num
          
sortList()
mylist[1][1] = "BINGO!"

print("Bingo Card Generator!")
print()
print(tabulate(mylist,tablefmt='grid'))


num = 0
while num<8:
  userGuess = int(input("Pick a number> "))
  for x in range(3):
    for y in range(3):
      if userGuess == mylist[x][y]:
        mylist[x][y] = "X"
        print(tabulate(mylist,tablefmt='grid'))
        num+=1

print("you won")
