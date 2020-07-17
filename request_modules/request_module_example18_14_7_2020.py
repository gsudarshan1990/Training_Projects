"""
This is another example of the request module
"""

import requests

def get_requests(baseurl,params,tag_string):

    params['tags']=tag_string
    response_object = requests.get(baseurl, params)
    print(response_object.url)
    #dict1 = response_object.json()
    #print(dict1)


base_url = 'https://api.flicker.com/services/rest/'
params ={}
params['api_key'] = 'flickr_key'
params['tag_mode'] = 'all'
params['method'] = 'flickr.photos.search'
params['per_page'] = 5
params['media'] = 'photos'
params['format'] ='json'
params['nojsoncallback'] =1

get_requests(base_url,params,"rivers,moutains")