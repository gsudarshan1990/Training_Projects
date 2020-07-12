"""
This is the example of the request module with functions and inbuilt
"""

import requests

def get_requests(base_url, params1):
    """
    This method is using functions to obtain the response object
    :param base_url: arg1 and string
    :param params1: arg2 and the dict
    :return:
    """
    response_object = requests.Request(method = 'GET', url = base_url, params=params1)
    response_object.url
    print(response_object.url)

pload = {'things':2, 'total':25}
get_requests('https://httpbin.org/get', pload )

