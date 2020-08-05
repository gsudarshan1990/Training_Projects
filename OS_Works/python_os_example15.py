"""
This program is to find the total number of files in the current directory
"""

import os

def count_python_files_in_directory(dirname):
    """This is used to count the total number of files in the directory"""
    if os.path.exists(dirname):
        count = 0
        for root, directory, files in os.walk(dirname):
            count += len([f for f in files if f.endswith(".py")])
        print('Total number of python files is {}'.format(count))



count_python_files_in_directory("E:\Training_Projects")
