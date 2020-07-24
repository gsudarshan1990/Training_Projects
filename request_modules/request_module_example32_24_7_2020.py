"""
This is another example of request module with different types of the status code
"""

import requests
from pprint import pprint

response_object = requests.get('http://example.com')
print(response_object.status_code)
print(response_object.ok)

bad_response_object = requests.get('https://yahoo.com/a1f2adfd5')
print(bad_response_object.status_code)
print(bad_response_object.ok)
print(bad_response_object.raise_for_status())