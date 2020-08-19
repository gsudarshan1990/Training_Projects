"""
This python program elaborates on the classmethod
"""
import math
class Circle:
    """This class provides the details related to the class"""
    all_circles = []
    def __init__(self, radius):
        """This is used to initialize the values"""
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        """This is used to find the area of the cirlce"""
        return math.pi*math.pow(self.radius,2)

    def perimeter(self):
        """This is used to find the perimeter of the circle"""
        return 2*math.pi*self.radius

    @classmethod
    def total_area(cls):
        """This provides the total area of all the circles"""
        cummulative_area = 0
        for c in cls.all_circles:
            cummulative_area+=c.area()
        return cummulative_area

    @classmethod
    def total_perimeter(cls):
        """This provides the total perimeter of all the circles"""
        cummulative_perimeter = 0
        for c in cls.all_circles:
            cummulative_perimeter+=c.perimeter()
        return cummulative_perimeter
