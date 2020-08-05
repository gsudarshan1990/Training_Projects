"""
This is another example of the os which is used to list the files on the directory
"""

import os

def list_files_in_directory(dirname):
    print('['+dirname+']')
    for filename in os.listdir(dirname):
        if not os.path.isdir(filename):
            print(filename)
        else:
            list_files_in_directory(filename)

list_files_in_directory("E:\Training_Projects\OS_Works")