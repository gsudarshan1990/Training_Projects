"""
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd.
"""

import os
import datetime

def file_date(filename):
    with open(filename,"w") as fh:
        fh.write("This first is created to read the time at which it was created")
    current_directory = os.getcwd()
    new_file = current_directory+"\\"+filename
    createdtime = os.path.getmtime(new_file)
    dt = datetime.datetime.fromtimestamp(createdtime)
    return dt.date()

print(file_date("newfile2.txt"))

