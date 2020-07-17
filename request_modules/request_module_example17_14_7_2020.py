"""
This is the another example of request module
"""

import requests

def get_requests(base_url,params):
    response_object = requests.get(base_url,params)
    dict1 = response_object.json()
    print(dict1)
    print(response_object.url)

base_url = 'https://itunes.apple.com/search'
parameters = {'term':'Ann Arbor', 'entity':'Podcast'}

get_requests(base_url,parameters)



