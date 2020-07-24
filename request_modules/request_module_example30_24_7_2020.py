"""
This is another example of the request module with the encoding
"""

import requests
from pprint import pprint

response_object = requests.get('https://github.com/timeline.json')
print(response_object.text)
print(response_object.encoding)
response_object.encoding ='ISO 8859-1'
print("Below is the text format after changing the encoding")
print(response_object.text)