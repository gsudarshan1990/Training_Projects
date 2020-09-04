#This is another python program


import math

class Circle:
    '''This class describes about the circle'''
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi*self.__radius*self.__radius

    def get_parameter(self):
        return 2*math.pi*self.__radius