"""
This is the request module which uses the head request
"""

import requests
from pprint import pprint
import webbrowser

response_object = requests.head('http://example.com')
print(response_object.status_code)
headers = response_object.headers
print(headers.keys())
print(headers['Content-Length'])