"""
This is another example of the decorator which checks the error
"""

import math

def area_circle_fn(radius):
    """
    This calculates the area of the circle
    :param radius: arg1 and integer
    :return: area and is float
    """
    return math.pi*radius*radius

def perimeter_circle_fn(radius):
    """
    This calculates the perimeter of the circle
    :param radius: arg1 and is integer
    :return: perimeter and is float
    """
    return 2*math.pi*radius

def diameter_circle_fn(radius):
    """
    This calculates the diameter of the circle
    :param radius: arg1 and is integer
    :return: diameter and is integer
    """
    return 2*radius


def check_radius(func):
    """
    This is the decorator which checks whether the radius is positive
    :param func: arg1 and is the function object
    :return: a function object
    """
    def inner_function(rad):
        if rad <=0:
            raise ValueError('Radius cannot be negative')
        return func(rad)
    return inner_function

find_area =check_radius(area_circle_fn)
print(find_area)
print(find_area(2))
#print(find_area(-1))