"""
This is another example of the os which creates the dictionary with filename as the key and timestamp as the value for a single directory
"""


import os
import datetime

def create_dictionary(dirname):
    data_of_files =dict()
    for name in os.listdir(dirname):
        filename = os.path.join(dirname,name)
        if os.path.isfile(filename):
            timestamp = os.path.getctime(filename)
            dt = datetime.datetime.fromtimestamp(timestamp)
            data_of_files[filename]=dt.ctime()
    for key, value in data_of_files.items():
        print(key,value)
    return data_of_files

print(create_dictionary("E:\Training_Projects\OS_Works"))