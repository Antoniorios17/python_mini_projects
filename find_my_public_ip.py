from requests import get



#find your public ip
def find_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    public_ip = 'My public IP address is: {}'.format(ip)
    return public_ip

while True:
    user_input= input("Do you want to get your public IP: (yes/no) ").split()[0].lower()
    if user_input == "y":
        print(find_ip())
