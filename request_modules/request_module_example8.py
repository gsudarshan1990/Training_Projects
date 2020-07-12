"""
This is the request parameter post example
"""

import requests
pload ={'username':'olivia', 'password':123}
response_object = requests.post('https://httpbin.org/post', data=pload)
print(response_object.url)
text = response_object.text
print(text)
dict1 =response_object.json()
print(dict1)
print(type(dict1))