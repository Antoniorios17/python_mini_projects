# This program validates usernames

def hint_username(username):
    if len(username) < 3 :
        print("Invalid username. Must be at least 3 charaters long")
    
    elif len(username) > 15:
        print("Invalid Username. Must be at most 14 characters long")
    else:
        print("Valid Username")

