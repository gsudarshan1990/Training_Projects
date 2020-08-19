"""
This python describes about the super class Shape
"""

class Shape:
    """This class describes about the shape"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltax, deltay):
        self.x+=deltax
        self.y+=deltay