"""
This uses the request module function options
"""

import requests
from pprint import pprint

response_option_object = requests.options('https://httpbin.org/get')
print(response_option_object.status_code)
print(response_option_object.text)
headers = response_option_object.headers
pprint(headers)