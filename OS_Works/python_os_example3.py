"""
This is the third OS example
"""


import os
"""
Accessing the files via os
"""
print(os.access('text1.txt',os.R_OK))
print(os.access('text1.txt',os.W_OK))
print(os.access('text1.txt',os.F_OK))
print(os.access('text1.txt',os.X_OK))


"""
Opening the files 
"""
fd = os.open('text1.txt',os.O_RDWR)
os.close(fd)

"""
creation of the duplicate file descriptor
"""

fd = os.open('text1.txt',os.O_RDWR)
d_fd = os.dup(fd)
os.close(d_fd)


print(os.pipe())

#temporary file

"""
tempfile = os.tmpfile()
tempfile.write('Temporary file is being written')
tempfile.seek(0)
print(tempfile.read())
tempfile.close()
"""

