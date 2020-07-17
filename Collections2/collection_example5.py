"""
This is example of the defaultdict

"""

from collections import defaultdict

defaultdict1 = defaultdict(lambda : 'Vanilla')
defaultdict1['Joe'] ='Strawberry'
defaultdict1['john'] ='Mango'
print(defaultdict1['james'])
print(defaultdict1)