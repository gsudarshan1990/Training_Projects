"""
Function to list files on in each folder of the current working directory
"""

import os

def list_files(dirname):
    """List the files on the working directory"""
    for root, dirs,files in os.walk(dirname,topdown=False):
        for file in files:
            print(os.path.join(root,file))

list_files("E:\Training_Projects\OS_Works")