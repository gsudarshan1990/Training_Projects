"""
This uses the requests module option put
"""

import requests
from pprint import pprint

response_put_object = requests.put('http://httpbin.org/put',data = {'key':'value'})
print(response_put_object.status_code)
print(response_put_object.text)