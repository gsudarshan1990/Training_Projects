"""
This is example of collections and is related to defaultdict

"""

from collections import defaultdict

defaultdict1 = defaultdict(lambda : 'vanilla')
defaultdict1['joe'] ='strawberry'
defaultdict1['sarah'] ='choco'
print(defaultdict1)
print(defaultdict1['james'])