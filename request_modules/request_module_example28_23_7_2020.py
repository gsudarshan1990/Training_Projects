"""
This is the request module with delete
"""

import requests
from pprint import pprint

response_delete_object = requests.delete('http://httpbin.org/delete')
pprint(response_delete_object.status_code)
pprint(response_delete_object.text)
pprint(response_delete_object.headers)