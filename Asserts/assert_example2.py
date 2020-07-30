"""
This is another example of the assert statement
"""

def square(x):
    return x**2

assert square(4) == 16

assert sorted([1,7,4]) == [1,4,7]
assert sorted([1,7,4],reverse=True) == [7,4,1]


#Calculating the distance between two points

import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


assert distance(1,2,1,2) == 0
assert distance(1,2,4,6) == 5
assert distance(0,0,1,1) == 2**0.5
