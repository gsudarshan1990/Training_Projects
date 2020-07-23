"""
This is example of request get with parameters
"""

import requests
import webbrowser
from pprint import pprint

response_obj = requests.get('https://www.wikipedia.org/')
print(response_obj.status_code)
print(response_obj.url)
webbrowser.open(response_obj.url)

URL = 'https://www.youtube.com/search'
PARAM = {'q':'skillsoft'}
webbrowser.open(URL)
response_obj2 = requests.get(url=URL, params=PARAM)
print(response_obj2.url)
print(response_obj2.is_redirect)
webbrowser.open(response_obj2.url)
headers = response_obj2.headers
print(headers['content-type'])
print(headers.keys())
