"""
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
"""

import os

def new_directory(directory,filename):
    """Creation of the new directory"""
    #check whether directory already exists
    if os.path.isdir(directory) == False:
        directorys = directory.split("\\")
        directory_name = directorys[-1]
        os.mkdir(directory_name)
    os.chdir(directory)
    with open(filename,"w") as fh:
        pass
    for root,directory,files in os.walk(directory):
        pass
    return len(files)


print(new_directory("E:\Training_Projects\OS_Works\\directoryviafunction",'fileviafunction.txt'))
