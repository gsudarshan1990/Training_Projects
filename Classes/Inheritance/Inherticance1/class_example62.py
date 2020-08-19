"""
This is another example of the Inheritance
"""

class Point:
    """This class describes about the Point"""
    def __init__(self, intX, intY):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY

    def __str__(self):
        """This represents the Point in the string format"""
        return "x ="+str(self.x)+" , y="+str(self.y)

class LabeledPoint(Point):
    """This class describes about the Labeled Point"""
    def __init__(self, intX, intY, label):
        """This is used to initialize the values"""
        super().__init__(intX,intY)
        self.label = label

    def __str__(self):
        """This represents the Label Point in the string format"""
        return "x ="+str(self.x)+" , y="+str(self.y)+" label ="+str(self.label)

p = Point(7,6)
lp = LabeledPoint(5,12,'Here')

print(p)
print(lp)


