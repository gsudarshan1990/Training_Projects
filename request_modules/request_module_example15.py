"""
This is one of the request module example along with the functions
"""

import requests

def get_rhymes(word):
    """
    This function gets the values from the REST API
    :param word: arg1 and string1
    :return: returns the list of words
    """
    base_url ='https://api.datamuse.com/words'
    param_dict ={}
    param_dict['rel_rhy'] = word
    param_dict['max'] = 3
    response_object = requests.get(base_url,param_dict)
    print(response_object.status_code)
    dict1 = response_object.json()
    return [d['word'] for d in dict1]

print(get_rhymes('funny'))