"""
Question 1
The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".
"""


import os
def create_python_script(filename):
    comments = "#Create a new python file and add this line to that file"
    current_directory = os.getcwd()
    new_file = current_directory+"\\"+filename
    with open(new_file,"w") as fh:
        fh.write(comments)
        file_size = os.path.getsize(new_file)
    return file_size

print(create_python_script('createdpython.py'))