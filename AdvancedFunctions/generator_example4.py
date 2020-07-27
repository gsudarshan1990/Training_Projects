"""
This is another example of the generator which creates the squares of the number
"""

def generate_square_number(square_limit):
    """
    This creates the generator object yielding squares of the number
    :param square_limit: arg1 and the maxmimum list
    :return: yields the square of the number
    """
    for i in range(0,square_limit):
        yield i**2

g = generate_square_number(10)
#print(list(g))
#print(tuple(g))
#print(set(g))
