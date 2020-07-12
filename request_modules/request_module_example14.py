"""
This is the example of using the parameters
"""

import requests
pload = {'q':'violins and guitars', 'r':'itbs'}
response_object = requests.get("https://google.com/search",params = pload)
print(response_object.url)
headers = response_object.headers
print(headers['content-type'])