"""
This is example of request module with version , copyright
"""

import requests
from pprint import pprint
import json

print(requests.__version__)
print(requests.__copyright__)
response= requests.get('https://www.metaweather.com/api/location/2487956/2018/11/28/')
print(type(response))
print(response.status_code)
headers = response.headers
print(type(headers))
pprint(headers)
print(headers['Allow'])
print(headers['content-type'])
print(type(response.text))
dict1 = json.loads(response.text)
print(dict1)
print(response.is_redirect)
