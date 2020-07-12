"""
This is the example of the request module which provides the data in the json format
"""

import requests

response_object = requests.get("https://api.datamuse.com/words?rel_rhy=funny")#This is the query parameter
dict_object = response_object.json()#This obtaining the dictionary
print(dict_object)