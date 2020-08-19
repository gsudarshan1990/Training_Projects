"""
This python program explains about the Inheritance
"""

class FourSideShape:
    """This class describes about the four sided shape"""
    def __init__(self, x, y):
        """This is used to initialize the values"""
        self.side1 = x
        self.side2 = y

    def area(self):
        """This provides the area of the Shape"""
        return self.side1*self.side2

class Rectangle(FourSideShape):
    """This class describes about the Rectangle which forms the is a relationship with FourSideShape"""
    def __init__(self, x ,y):
        FourSideShape.__init__(self, x, y)

class Square(Rectangle):
    """This class describes about the Square which forms the is a relationship with Rectangle"""
    def __init__(self, x):
        Rectangle.__init__(self, x, x)

s1 = Square(4)
print(s1.area())
r1 = Rectangle(2,3)
print(r1.area())