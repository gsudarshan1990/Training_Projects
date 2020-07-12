"""
This is the example of cookies
"""

import requests
response_object = requests.get('http://example.com/some/cookie/setting/url')
cookies = response_object.cookies
print(cookies)