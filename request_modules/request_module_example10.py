"""
This is the request module delete example
"""

import requests
pload = {'things':2, 'total':25}
response_object = requests.delete('https://httpbin.org/delete', params = pload)
print(response_object.url)
dict1 = response_object.json()
print(dict1)