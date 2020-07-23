"""
This is another example of request module
"""

import requests
from pprint import pprint
import json

response = requests.get('http://swapi.co/api/planets/3')
print(response.status_code)
print(type(response))
header = response.headers
print(header)
print(header['content-type'])
print('Allow' in header)
print(response.is_redirect)
