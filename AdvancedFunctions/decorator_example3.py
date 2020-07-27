"""
This is another example of the decorator
"""
import math

def safe_calculater_all(func):
    """
    This is the outer decorator
    :param func: arg1 and is function
    :return: function object
    """
    def inner_function(*args):
        for arg in args:
            if arg <=0:
                raise ValueError('Value cannot be negative')
        return func(*args)
    return inner_function


@safe_calculater_all
def area_circle_fn(radius):
    return math.pi*radius*radius

@safe_calculater_all
def area_rectangle_fn(length,breadth):
    return length*breadth

print(area_circle_fn(10))
print(area_rectangle_fn(2,3))

#print(area_circle_fn(-1))
#print(area_rectangle_fn(2,-3))
