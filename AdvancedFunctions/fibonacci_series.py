"""
This is the python program which provides the fibonacci series
"""

def fibonacci(a,b):
    """
    This is the fibonacci series
    :param a:  arg1 and first number
    :param b: arg2 and second number
    :return: Nothing
    """
    print(a,b,end =" ")
    while a<50:
        a,b = a+b, a
        print(a, end =" ")

print(fibonacci(1,1))