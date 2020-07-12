"""
This is the example of request module which provides information related to header
"""

import requests

response_object = requests.get("https://www.google.com")
#Obtaining the header information
response_object_headers = response_object.headers
print(response_object_headers)
print(response_object_headers['content-type'])