"""
This is the examnple of the bad status code
"""

import requests
response_object = requests.get('https://httpbin.org/status/404')
print(response_object.status_code)