"""
This is another example of os
"""

import os
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')