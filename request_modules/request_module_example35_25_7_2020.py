"""
This is another example of requests with redirects
"""

import requests
from pprint import pprint

response_object = requests.get("http://gmail.com")
print(response_object.status_code)
print(response_object.url)
print(response_object.history)

print('If the response is re-directed')

if response_object.history:
    print('Request redirected')
    for resp in response_object.history:
        print(resp.url)

    print('Final Destination')
    print(response_object, response_object.url)
else:
    print('Request Not Directed')

print('Final Destionation redirect', response_object.is_redirect)
print('Final Destionation permanent redirect', response_object.is_permanent_redirect)

print('Other Redirect')
print(response_object.history[0].is_redirect)