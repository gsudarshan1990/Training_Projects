"""
This is another example of the composition
"""

class Point:
    """This class represents the Point"""
    def __init__(self, intX, intY):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY

    def distanceFromOrigin(self):
        """This function is used to calculate the function from the origin"""
        return  ((self.x)**2+(self.y)**2)**0.5

    def __str__(self):
        """This function prints the point in the string format"""
        return "x ="+str(self.x)+" ,y="+str(self.y)

class Rectangle:
    """This class represents the rectangle along with the composition"""
    def __init__(self, intX, intY, length, breadth):
        """This is used to initialize the values and perform other operations"""
        self.point = Point(intX, intY)
        self.length = length
        self.breadth = breadth
        if (intX<length) and (intY<breadth):
            print('Point is inside the rectangle')

    def distanceFromOrigin(self):
        """This is used to calculate the distance from origin"""
        return self.point.distanceFromOrigin()

    def __str__(self):
        """This represents the rectangle"""
        return str(self.point)+" length="+str(self.length)+" breadth="+str(self.breadth)

r = Rectangle(2,3,5,7)
print(r.distanceFromOrigin())
print(r)
