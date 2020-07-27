"""
This is used to find the factorial of the a number using the recursive
"""

def factorial(number):
    """
    This is used to find the factorial of a number1
    :param number: arg1 and number integer
    :return: total factorial
    """
    if number<0:
        print('Sorry, Recursive does not exist for the negative number')
        return
    if number  == 0:
        return 1
    result = number*factorial(number-1)
    return result

print(factorial(5))