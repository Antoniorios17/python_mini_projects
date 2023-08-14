from requests import get

#This program will find your current public IP address

def find_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    public_ip = 'Your public IP address is: {}'.format(ip)
    return public_ip

while True:
    print("=========================")
    print("Welcome to the IP Finder")
    print("=========================\n\n")
    user_input= input("Do you want to get your public IP: (yes/no) ")
    if user_input.split()[0].lower() == "y":
        print(find_ip())
        print("")
        user_entry = input("Would you like to continue(yes/no): ")
        if user_entry.lower().split()[0] == "y":
            continue
        else:
            print("Thank you, Goodbye!")
            print("")
            break
    else:
        print("Thank you, Good bye! ")
        break

