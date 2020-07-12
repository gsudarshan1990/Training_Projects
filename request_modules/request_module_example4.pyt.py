"""
This is the example of the request module which obtains the url
"""

import requests

response_object = requests.get("https://status.github.com/api/status.json")
url = response_object.url
print(url)