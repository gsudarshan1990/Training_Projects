"""
This is example post request including the file
"""

import requests
import pprint

URL = 'http://httpbin.org/post'
files = {'files':open('text.txt','rb')}
json1 = {'upload_file':'text.txt','OUT':'csv'}

response_object = requests.post(url=URL, files=files, data=json1)
print(response_object.status_code)
print(response_object.is_redirect)
print(response_object.text)
