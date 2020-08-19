"""
This class explains about the class variables
"""
import math
class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi*(self.radius)**2

c1 = Circle(7)
print(c1.area())
print(Circle.pi)# Accessing by the Classname
print(c1.pi)#Accessing by the Instance name