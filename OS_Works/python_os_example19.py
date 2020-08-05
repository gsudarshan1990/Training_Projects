"""
Function to remove the file
"""

import os

def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
        print('File is removed')
    else:
        print('{} is not found'.format(filename))

remove_file("E:\Training_Projects\OS_Works\\text2.txt")
remove_file("E:\Training_Projects\OS_Works\\text3.txt")