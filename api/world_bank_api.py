import requests
from requests.exceptions import ConnectionError, HTTPError
import json

# response = requests.get("https://api-server.dataquest.io/economic_data/countries")

# data = json.loads(response.json())
# # print((data[0].keys()))

# for key, value in data[0].items():
#     print(f'{str(key):50}  {str(value):10}')


try:    
    r = requests.get("https://api-server.dataquest.io/economic_data/countries")
    r.raise_for_status()
    print(r.status_code)

except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}')