"""
This is the comprehensive request module
"""

import requests

response_object = requests.get("https://api.github.com")
print(type(response_object))
status_code = response_object.status_code
if status_code == 200:
    print('This request is successful')
elif status_code == 404:
    print('This request is unsuccessfulr')
url = response_object.url
print(url)
text = response_object.text[:150]
print(text)
dict_object = response_object.json()
print(dict_object)
headers = response_object.headers
print(headers)
print(headers['content-type'])

