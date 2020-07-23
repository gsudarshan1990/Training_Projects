"""
This is the example of the post request
"""

import requests
import pprint
import webbrowser

URL = 'https://en.wikipedia.org/w/index.php'
data1 = {'search':'skillsoft'}

response_object = requests.post(url=URL, data =data1)
print(response_object.url)
headers = response_object.headers
text = response_object.text
print(headers)

with open('skillsoft.html','wb') as f:
    for chunk in response_object.iter_content(chunk_size=10000):
        f.write(chunk)

webbrowser.open('skillsoft.html')