"""
Request module put and delete
"""

import requests
response_object = requests.put('https://httpbin.org/put')
headers = response_object.headers
print(headers)
print(response_object.text)
dict1 = response_object.json()
print(dict1)