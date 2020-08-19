"""
This is another example of the inheritance
"""

class Point:
    """This class explains about the Point """
    def __init__(self, intX, intY):
        """This is used to intialize the values"""
        self.x = intX
        self.y = intY

    def distanceFromOrigin(self):
        """This is used to calculate the distance from the origin"""
        return ((self.x)**2+(self.y)**2)**0.5

    def __str__(self):
        """This is used to represent the point in the string format"""
        return "x ="+str(self.x)+" ,y="+str(self.y)

class LabeledPoint(Point):
    """This is about the Point which can be labeled"""
    def __init__(self, intX, intY, label):
        """This is used to initialize the values"""
        super().__init__(intX,intY)
        self.label = label

    def __str__(self):
        """This represents the string in the labeled format"""
        return super().__str__()+" label="+str(self.label)

p = LabeledPoint(7,6,"there")
print(p.distanceFromOrigin())
print(p)