
listOfShame = [['frank','25', 'micro'], ['joe', '33', 'apple']] 

while True: 
  menu = input("Add or Remove?") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    

  else: 
    name = input("What is the name of the record to delete?") 
    for sublist in listOfShame:
      if name in sublist: 
        listOfShame.remove(sublist) # remove the whole row if name is in it


  print(listOfShame)