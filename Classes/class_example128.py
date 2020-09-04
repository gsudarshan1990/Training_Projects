#This is another python program


class Shape:
    '''This class describes about the Shape of the polygon'''
    def __init__(self, shape_type, color ='red'):
        self.shape_type = shape_type
        self.color = color

    def get_type(self):
        return self.shape_type

    def get_color(self):
        return self.color

    def get_area(self):
        pass

    def get_parameter(self):
        pass

import math
class Circle(Shape):

    def __init__(self, shape_type, color, radius):
        Shape.__init__(self, shape_type, color)
        self.__radius = radius

    def get_area(self):
        return math.pi*self.__radius*self.__radius

    def get_perimeter(self):
        return 2*math.pi*self.__radius

circle = Circle('circle','blue',10)

print(circle.get_color())
print(circle.get_area())
