"""
This page contains the recursive and non recursivefunctions
"""

"""
This is non recursive
"""

def decrement(num):
    """
    This decrements the number provided as argument by 1
    :param num: arg1 and int
    :return: nothing
    """
    while num>0:
        print(num)
        num = num -1

#decrement(10)

"""
Illustrating the above decrement with the use of the recursive function
"""

def decrement(num):
    if num == 0:
        return
    print(num)
    decrement(num-1)

decrement(10)

"""
Below is the another recursive function with the terminating condition
"""

def recursive_sum(num):
    """
    This function provides the sum of the numbers between num and 1
    :param num: arg1 and the initial number
    :return: total sum
    """
    if num == 0:
        return 0
    result = num+recursive_sum(num-1)
    return result

print(recursive_sum(10))
