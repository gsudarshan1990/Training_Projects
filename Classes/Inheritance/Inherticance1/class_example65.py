"""
This class describes about the composition
"""

class Point:
    """This class describes about the Point"""
    def __init__(self, intX, intY):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY

    def distanceFromOrigin(self):
        """This is used to obtain the distance from the origin"""
        return ((self.x)**2+(self.y)**2)**0.5

    def __str__(self):
        """This represents the Point in the string format"""
        return "x ="+str(self.x)+" ,y="+str(self.y)

class LabeledPoint:
    """Composition is explained in this class"""
    def __init__(self, intX, intY, label ):
        self.point = Point(intX, intY)
        self.label = label

    def distanceFromOrigin(self):
        return self.point.distanceFromOrigin()

    def __str__(self):
        return str(self.point)+" label="+str(self.label)

p = LabeledPoint(7,6, 'here')
print(p.distanceFromOrigin())
print(p)