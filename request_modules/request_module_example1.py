"""
This is the example of the request module with the successful request
"""

#This imports the request
import requests

#creating the response object
response_object = requests.get("https://www.google.com/") #This is a sample url without query parameter
print("Below mentions the status code is successful or not")
print(response_object.status_code)
if response_object.status_code == 200:
    print('This is successful request')
elif response_object.status_code == 404:
    print('This is failure request')

