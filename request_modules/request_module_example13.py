"""
This is the example of status code redirect
"""

import requests
response_object = requests.get('https://www.example.com/old1234.html')
print(response_object.status_code)
print(response_object.url)