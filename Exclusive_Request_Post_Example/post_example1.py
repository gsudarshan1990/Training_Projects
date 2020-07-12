"""
This is the request module post example
"""

import requests
import json
dict1 = {'things':2, 'total':25}
response_object = requests.post('https://api.github.com/some/endpoint', data=json.dumps(dict1))
print(response_object.url)
dict2 = response_object.json()
print(dict2)
