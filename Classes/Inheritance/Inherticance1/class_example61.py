"""
This explains the inheritance
"""

class Point:
    """This describes the Point"""
    def __init__(self, x, y):
        """This is used to initialize the values"""
        self.x = x
        self.y = y

    def distanceFromOrigin(self):
        """This is used to return the distance from the Origin"""
        return ((self.x)**2+(self.y)**2)**0.5

    def __str__(self):
        """This is used to represent the point in the string format"""
        return "x="+str(self.x)+" , y="+str(self.y)

class LabeledPoint(Point):
    pass

p = LabeledPoint(7,6)
print(p.distanceFromOrigin())
print(p)