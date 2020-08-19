"""
This is another example of the inheritance
"""

class Shape:
    """This class describes about the shape"""
    def __init__(self, x, y):
        """This is used to initialize the values"""
        self.x = x
        self.y = y


class Square(Shape):
    """This class describes about the Square which forms the is a relationship with class Shape"""
    def __init__(self, side, x, y):
        """This is used to initialize the values"""
        self.side = side
        self.x = x
        self.y = y

class Circle(Shape):
    """This class describes about the Circle which forms the is a relationship with Shape"""
    def __init__(self, radius, x, y):
        """This is used to initialize the values"""
        self.radius = radius
        self.x = x
        self.y = y