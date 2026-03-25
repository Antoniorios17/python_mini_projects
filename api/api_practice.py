import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

# print(response.status_code)

# dict_keys(['items', 'has_more', 'quota_max', 'quota_remaining'])
data = response.json()
# print(data["items"][0])

# for item in data["items"]:
#     print(item)

# print(data["items"][0]["owner"]["display_name"])

for item in data["items"]:
    print(f'user_id: {item["owner"]["user_id"]:10} | username is: {item["owner"]["display_name"]:10}')
    # print(f'username is: {item["owner"]["display_name"]}')