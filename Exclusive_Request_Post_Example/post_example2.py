"""
This is the second post example
"""

import requests
sample_object = {'things':2, 'total':25}
response_object = requests.post('https://api.github.com/some/endpoint', json=sample_object)
print(response_object.headers)
dict2 = response_object.json()
print(dict2)