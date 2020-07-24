"""
This is another example fo requests with exceptions
"""

import requests
from requests import exceptions
from pprint import pprint

try:
    response_object = requests.get('http://nonexistent.com')
except exceptions.ConnectionError:
    pprint('Error : ConnectionError')

try:
    response_object2 = requests.get('http://github.com', timeout = 0.01)
except (exceptions.ConnectTimeout , exceptions.ConnectionError) as e:
    pprint('Error: ConnectTimeOut')