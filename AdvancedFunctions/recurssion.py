"""
This is the example of the recursion
"""

def hello(name):
    """
    This is the recurssive functiokn
    :param name: arg1 and string
    :return: nothing
    """
    print("Hello", name)
    hello(name)

#hello('son')

import sys
print(sys.getrecursionlimit())

def increment(number):
    print(number, end =" ")
    increment(number+1)

#increment(1)

sys.setrecursionlimit(100)

#increment(1)

sys.setrecursionlimit(1000)