"""
This is another example of the OS.PATH
"""

import os
import datetime

print(os.path.sep)
print(os.path.basename("E:\\Training_Projects\\Unittest_Example"))
print(os.path.dirname("E:\\Training_Projects\\Unittest_Example"))
print(os.path.join("E:\\Training_Projects","New_project"))
print(os.path.split("E:\\Training_Projects\\Unittest_Example"))
print(os.path.exists("E:\\Training_Projects\\Unittest_Example"))
print(os.path.isfile("E:\\Training_Projects\\credentials.txt"))
print(os.path.isdir("E:\\Training_Projects\\Selenium_With_Unittest"))

print("size",os.path.getsize("text1.txt"))
print("created time",datetime.datetime.fromtimestamp(os.path.getctime("text1.txt")))
print("modified time", datetime.datetime.fromtimestamp(os.path.getmtime("text1.txt")))
print("appended time", datetime.datetime.fromtimestamp(os.path.getatime("text1.txt")))
print("absolute path for the file ", os.path.abspath("text1.txt"))