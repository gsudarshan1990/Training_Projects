"""
This is an example of of os.walk
"""

import os
path = "E:\\Training_Projects\\OS_Works\\oswalk"
#print(next(os.walk(path)))

#print(list(os.walk(path)))
#[('E:\\Training_Projects\\OS_Works\\oswalk', ['hello'], ['abc123.txt']), ('E:\\Training_Projects\\OS_Works\\oswalk\\hello', [], ['abc.txt', 'def.txt'])]

#print(list(os.walk(path)))
#[('E:\\Training_Projects\\OS_Works\\oswalk', ['hello', 'world'], ['abc123.txt']), ('E:\\Training_Projects\\OS_Works\\oswalk\\hello', [], ['abc.txt', 'def.txt']), ('E:\\Training_Projects\\OS_Works\\oswalk\\world', [], ['123.txt', '456.txt'])]

#obtaining in the form of the tuple
"""
for each in os.walk(path):
    print(each)
"""
"""
[('E:\\Training_Projects\\OS_Works\\oswalk', ['hello', 'world'], ['abc123.txt']), ('E:\\Training_Projects\\OS_Works\\oswalk\\hello', [], ['abc.txt', 'def.txt']), ('E:\\Training_Projects\\OS_Works\\oswalk\\world', [], ['123.txt', '456.txt'])]
('E:\\Training_Projects\\OS_Works\\oswalk', ['hello', 'world'], ['abc123.txt'])
('E:\\Training_Projects\\OS_Works\\oswalk\\hello', [], ['abc.txt', 'def.txt'])
('E:\\Training_Projects\\OS_Works\\oswalk\\world', [], ['123.txt', '456.txt'])

"""

for root,directory,files in os.walk(path,topdown=False):
    #print(root)
    #print(directory)
    #print(files)
    pass

"""
root
E:\Training_Projects\OS_Works\oswalk
E:\Training_Projects\OS_Works\oswalk\hello
E:\Training_Projects\OS_Works\oswalk\world
"""

"""
directory
['hello', 'world']
[]
[]
"""

"""
files
['abc123.txt']
['abc.txt', 'def.txt']
['123.txt', '456.txt']

"""

"""
topdown = False
E:\Training_Projects\OS_Works\oswalk\hello
[]
['abc.txt', 'def.txt']
E:\Training_Projects\OS_Works\oswalk\world
[]
['123.txt', '456.txt']
E:\Training_Projects\OS_Works\oswalk
['hello', 'world']
['abc123.txt']
"""
"""
for root,directory,files in os.walk(path,topdown=False):
    if len(files)!=0:
        print(root)
        for each in files:
            print(each)
"""

"""
E:\Training_Projects\OS_Works\oswalk\hello
abc.txt
def.txt
E:\Training_Projects\OS_Works\oswalk\world
123.txt
456.txt
E:\Training_Projects\OS_Works\oswalk
abc123.txt

"""

for root,directory,files in os.walk(path):
    if len(files)!=0:
        for each in files:
            print(os.path.join(root,each))
"""
E:\Training_Projects\OS_Works\oswalk\abc123.txt
E:\Training_Projects\OS_Works\oswalk\hello\abc.txt
E:\Training_Projects\OS_Works\oswalk\hello\def.txt
E:\Training_Projects\OS_Works\oswalk\world\123.txt
E:\Training_Projects\OS_Works\oswalk\world\456.txt

"""