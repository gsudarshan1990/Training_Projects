"""
This module is about exploration of the OS module
"""

import os
print(os.getcwd())
print(os.listdir())
os.mkdir('Python1')
os.rmdir('Python1')
print(os.environ)
print(os.getlogin())
print(os.cpu_count())
print(os.name)
