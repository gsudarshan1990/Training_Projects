"""
This is example of the request module with the encoding
"""

import requests
from pprint import pprint
import webbrowser

response_object =requests.get('http://httpbin.org/')
print(response_object.status_code)
print(response_object.encoding)
#print(response_object.text)
response_object.encoding = 'ISO 8859-1'
print(response_object.encoding)

with open("secondfile.html","wb") as f:
    """This is used to write the response details
    """
    for chunk in response_object.iter_content(chunk_size=10000):
        f.write(chunk)

webbrowser.open("secondfile.html")