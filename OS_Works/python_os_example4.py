"""
This is another os example
"""

import os
import os.path
print(os.path.join(os.sep, 'home','user','work'))

print(os.path.curdir)
print(os.getcwd())

print(os.path.isdir('foo'))
print(os.path.isfile('text1.txt'))
print(os.path.getsize('text1.txt'))

print(os.path.exists('foo'))



print(os.environ)
print(os.environ.keys())

print(os.path.basename('E:\Training_Projects\OS_Works'))
print(os.path.dirname('E:\Training_Projects\OS_Works'))