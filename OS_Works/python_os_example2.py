"""
This is the example of os modules

"""

import os

curr_dir = os.getcwd()
print(curr_dir)

os.chdir(os.path.join(curr_dir, 'foo'))
print(os.getcwd())

print(os.path.split(curr_dir))
print(os.path.splitext('foo.jpg'))
filename1, filename2 = os.path.split(curr_dir)
print(os.path.join(filename1,filename2))

