"""
This is another example of the requests re-direct
"""

import requests
from pprint import pprint

response_object = requests.get('http://gmail.com', allow_redirects= False)
pprint(response_object.status_code)
pprint(response_object.history)

print("Usage of the head")

response_object2 = requests.head('http://google.com', allow_redirects= True)
pprint(response_object2.status_code)
pprint(response_object2.history)

response_object3 = requests.head('http://google.com')
print(response_object3.status_code)
print(response_object3.history)

from requests import exceptions
try:
    response_object4 = requests.get("https://github.com", timeout = 0.01)
except exceptions.ConnectTimeout:
    print('Connection Could not established')

response_object5 = requests.get('https://github.com', timeout =(5,18))

response_object6= requests.get('https://github.com', timeout = None)