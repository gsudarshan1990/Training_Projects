"""
This is another example of the inheritance
"""

class Point:
    """This class describes the Point"""
    def __init__(self, intX, intY):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY

    def distanceFromOrigin(self):
        """This is used to calculate the distance from the origin"""
        return ((self.x)**2+(self.y)**2)**2

    def __str__(self):
        """This represents the point in the string format"""
        return "x ="+str(self.x)+" , y="+str(self.y)

class LabeledPoint(Point):
    """This class inherits the LabelPoint"""
    def __init__(self, intX, intY, label):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY
        self.label = label

    def __str__(self):
        """This represents the point in the string format"""
        return "x= "+str(self.x)+" y= "+str(self.y)+" label="+str(self.label)

p = Point(5,6)
lp = LabeledPoint(7, 12, 'there')
print(p)
print(lp)
