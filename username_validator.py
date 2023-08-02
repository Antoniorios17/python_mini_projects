# This program validates usernames
# username needs to be at least 3 characters

def hint_username(username):
    
    if len(username) < 3 :
        print("Invalid username. Must be at least 3 charaters long")
    
    elif len(username) > 14:
        print("Invalid Username. Must be at most 14 characters long")
    else:
        print("Valid Username")

hint_username("mike")
hint_username("22")
hint_username("Thisismyusername")


