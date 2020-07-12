"""
This is the second context manager example
"""

from contextlib import contextmanager

@contextmanager
def OpenFile(filename,mode):
    f = open(filename,mode)
    yield f
    f.close()


with OpenFile("E:\sample_file.txt.txt", 'r') as file_header:
    print(file_header.readline())