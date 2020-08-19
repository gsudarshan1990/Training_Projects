"""
This class contains the static methods
"""

import math
class Circle:
    """This class provides descrition related to the class"""
    all_circles = []
    pi = math.pi

    def __init__(self, radius):
        """This is used to initialize the values"""
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        """This is used to provide the area of the particular circle"""
        return self.pi*(pow(self.radius,2))

    @staticmethod
    def total_area():
        """This represents the total area of the cirlces"""
        total=0
        for c in Circle.all_circles:
            total=total+c.area()
        return total
