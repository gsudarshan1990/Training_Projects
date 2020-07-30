"""
This is used to test the class
"""

import math

class Point:
    """
    This class represents the co-ordinates in the graph
    """
    def __init__(self, x, y):
        """
        This is used to initialize the values
        :param x: arg1 and first co-ordinate
        :param y: arg2 and second co-ordinate
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt((self.x)**2+(self.y)**2)

    def move(self,new_x,new_y):
        """
        This re-locates the point to the new location
        :param new_x: arg1 and distance to be moved in the x direction
        :param new_y: arg2 and distance to be movied in the y direction
        :return: nothing
        """
        self.x = self.x + new_x
        self.y = self.y + new_y

p = Point(3,4)
assert p.x == 3
assert p.y == 4

assert p.distance_from_origin() == 5.0

p.move(-2,3)

assert p.x == 1
assert p.y == 7