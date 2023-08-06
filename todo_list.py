
def additem(tdlist):
  """Adds Name of Task, Due Date, & Priority to To-Do List"""
  task = input("What is your ToDo item? ")
  DueDate = input("When is this due (MM/DD/Year)? ")
  Priority = input("What is the priority of this todo item (Low, Medium, High)? ")
  newrow = [task,DueDate, Priority]
  tdlist.append(newrow)
  return tdlist

def viewpriority(priority, tdlist):
  prioritylist = []
  for item in range(len(tdlist)):
      if tdlist[item][2][0].lower() == priority:
        prioritylist.append(tdlist[item])
  return prioritylist

def editList(tdList):
    ## print the list have them select a list
  for item in range(len(tdList)):
    print(f"{item}. {tdList[item]}")
  item_to_edit = int(input("Which item would you like to edit?: "))
  # list_edit = input("Provide edited list:")
  tdList.pop(item_to_edit) ## remove at the index
  task = input("What is your ToDo item? ")
  DueDate = input("When is this due (MM/DD/Year)? ")
  Priority = input("What is the priority of this todo item (Low, Medium, High)? ")
  newrow = [task,DueDate, Priority]
  tdList.insert(item_to_edit,newrow)
  print(tdList)
  

## For loop from 0 to range(len(todolist))
    ## ask user for key. 
    ## affter selecting list, prompt them for new list
    ## change list and print

def removeItem():
  for i in range(len(todoList)):
    print(f'{i+1}) {todoList[i][0]}')
  complete = input("Which item is complete?")
  for item in range(len(todoList)):
    if complete == todoList[item][0]:
      print(complete)
      print("Item complete!")
      todoList.pop(item)
      break
    else:
      doubleCheck = input(f"{complete} doesn't exist - Add it to your Todo list? ").strip().lower()[0]
      if doubleCheck == 'y':
        additem()
      else:
        print("Ok see you later")
        break
      
      
      
  
# todoList=[]
todoList = [["task 1","07/30","H"],["task 2","07/30","L"],["task 3","12/25","M"]]
while True:
  userSays = input("Do you want add, view, remove, or edit your ToDo list?: ")
  if userSays.strip().lower()[0] == 'a':
    todoList = additem(todoList)
    print(todoList)
  elif userSays.strip().lower()[0] == 'v':
    userView = input("View All or view priorities (L, M, H)? ").strip().lower()[0]
    if userView == 'a':
      print(todoList)
    else: #elif userView.strip().lower()[0] != 'a':
      priority = userView
      prioritylist = viewpriority(userView, todoList)
      print(prioritylist)
  elif userSays.strip().lower()[0] == 'e':
    editList(todoList)
  elif userSays.strip().lower()[0] == 'r':
    removeItem()
  else:
    break
  
    
# def additem(tdlist):
#   """Adds Name of Task, Due Date, & Priority to To-Do List"""
#   tdlist = []
#   task = input("What is your ToDo item? ")
#   DueDate = input("When is this due (MM/DD/Year)? ")
#   Priority = input("What is the priority of this todo item (Low, Medium, High)? ")
#   newrow = [task,DueDate, Priority]
#   tdlist.append(newrow)
#   return tdlist

# def viewpriority(priority, tdlist):
#   prioritylist = []
#   for item in range(len(tdlist)):
#       if tdlist[item][2] == priority:
#         prioritylist.append(tdlist[item])
#   return prioritylist


