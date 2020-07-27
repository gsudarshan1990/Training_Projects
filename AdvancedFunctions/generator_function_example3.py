"""
This is another example of the generator
"""

def generate_even_number(limit):
    """
    This generates the even number
    :param limit: arg1 and maximum limit
    :return: nothing
    """
    for i in range(0, limit, 2):
        yield i

g = generate_even_number(11)
"""
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

l = list(g)
print(l)