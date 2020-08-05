"""
This is used to check whether the file is a file and return the size of the file
"""

import os

def information_about_file(filename):
    if os.path.isfile(filename):
        print("Is is file",os.path.isfile(filename))
        print("Size of the file ", os.path.getsize(filename))
    else:
        print('Is it file',os.path.isfile(filename))
        print("File not found")

information_about_file("text1.txt")
print("*"*20)
information_about_file("text10.txt")