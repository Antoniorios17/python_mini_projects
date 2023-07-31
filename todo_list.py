def additem(tdlist):
  """Adds Name of Task, Due Date, & Priority to To-Do List"""
  tdlist = []
  task = input("What is your ToDo item? ")
  DueDate = input("When is this due (MM/DD/Year)? ")
  Priority = input("What is the priority of this todo item (Low, Medium, High)? ")
  newrow = [task,DueDate, Priority]
  tdlist.append(newrow)
  return tdlist

def viewpriority(priority, tdlist):
  prioritylist = []
  for item in range(len(tdlist)):
      if tdlist[item][2] == priority:
        prioritylist.append(tdlist[item])
  return prioritylist
  


todoList = [["task 1","07/30","H"],["task 1","07/30","L"],["task 3","12/25","M"]]
while True:
  userSays = input("Do you want add, view, remove, or edit your ToDo list?")
  if userSays.strip().lower()[0] == 'a':
    todoList = additem(todoList)
    print(todoList)
  if userSays.strip().lower()[0] == 'v':
    userView = input("View All or view priorities (L, M, H)? ")
    if userView.strip().lower()[0] == 'a':
      print(todoList)
    else: #elif userView.strip().lower()[0] != 'a':
      prioritylist = viewpriority(userView, todoList)
      print(prioritylist)
    