"""
This is used to post data to the website and view it
"""

import requests
import webbrowser
from pprint import pprint

URL = 'https://pastebin.com/api/api_post.php'
API_KEY = '5d8660647287b565c47e269086deceeb'
payload = "{'user':'john', 'email':'john@john.com'}"

parameters ={'api_dev_key':API_KEY,
             'api_option':'paste',
             'api_paste_code':payload,
             'api_paste_format':'python'
}

response_object = requests.post(url=URL, data = parameters)

print(response_object.url)

if response_object.status_code ==200:
    pprint('Your request is successful')
    pprint('You can view on the website {}'.format(response_object.text))
else:
    pprint('Your request is unsuccessful')

webbrowser.open(response_object.text)
