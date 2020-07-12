"""
Passing the parameters in the get requests
"""



import requests
pload ={'things':2, 'total':25}
response_object = requests.get('https://httpbin.org/get', pload)
print(response_object.url)
print(response_object.text)
headers = response_object.headers
print(headers)
