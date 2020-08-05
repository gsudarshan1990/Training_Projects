"""
This is python os function which classifies the directories and files in a give directory
"""

import os

def classify_files_directories(dirname):
    list1 = os.listdir(dirname)
    #print(list1)
    for name in list1:
        path1 = os.path.join(dirname,name)
        if os.path.isdir(path1):
            print('{} is a directory'.format(path1))
        else:
            print('{} is a file'.format(path1))

classify_files_directories("E:\Training_Projects\OS_Works")