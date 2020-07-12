"""
This is the example of the request module with a text response with the html page
"""

import requests

response_object = requests.get("https://www.google.com")
response_object_text = response_object.text[:200]
print(type(response_object_text))
print(response_object_text)
