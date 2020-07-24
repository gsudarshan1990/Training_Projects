"""
This is example of the requests module to handle json formats
"""

import requests
from pprint import pprint

response_object = requests.get('https://api.github.com/events')
headers = response_object.headers
print(headers['content-type'])
dict1= response_object.json()
print(dict1)

try:
    response_object2 = requests.get('http://www.yahoo.com')
    print(response_object2.status_code)
    print(response_object2.ok)
    print(response_object2.json())
except:
    pprint('No JSON FORMAT')


with requests.get('https://api.github.com/events', stream = True) as response:
    with open('jsonresponse.txt','wb') as f:
        for chunk in response.iter_content(chunk_size=1000):
            f.write(chunk)

