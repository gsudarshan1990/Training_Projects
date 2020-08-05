"""
This is an example of the which uses the os module which creates the dictionary with filename and value the time of creation recursively for all the files
in a directory
"""

import os
import datetime
import collections

def create_dictionary_for_list_of_files(dirname):
    data = collections.defaultdict(list)
    for root,dir,filenames in os.walk(dirname):
        for filename in filenames:
            fullname = os.path.join(root,filename)
            size = os.path.getsize(fullname)
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(fullname))
            data[fullname] = (size,creation_time.ctime())
    for key,value in data.items():
        print(key)
        print(value)
        print()
    return data

create_dictionary_for_list_of_files("E:\Training_Projects\OS_Works")