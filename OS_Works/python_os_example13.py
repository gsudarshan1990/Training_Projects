"""
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
"""

import os

def parent_directory():
    """
    This provides the parent directory for the current working directory
    :return: relative path  for the directory
    """
    current_directory = os.getcwd()
    os.chdir("..")
    relative_path = os.getcwd()
    return relative_path

print(parent_directory())