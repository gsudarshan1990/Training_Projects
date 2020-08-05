"""
This is an example to search the directory
"""

import os
import platform
import string

req_files = input('Enter the file to be searched')


if platform.system() == 'Windows':
    pd_names = string.ascii_uppercase
    ad_names = []
    for each_drive in pd_names:
        if os.path.exists(each_drive+"://"):
            ad_names.append(each_drive+"://")
    #print(ad_names)
    for each_drive in ad_names:
        for root,directory, files in os.walk(each_drive):
            for each_file  in files:
                if each_file == req_files:
                    print(os.path.join(root,each_file))
else:
    for root, directory, files in os.walk("/"):
        for each_file in files:
            if each_file == req_files:
                print(os.path.join(root,each_file))