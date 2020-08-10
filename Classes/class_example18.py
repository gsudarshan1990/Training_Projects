"""
This is another example of the class

We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a Rectangle class using this idea. To create a Rectangle object at location (4,5) with width 6 and height 5, we would do the following:
Add the following accessor methods to the Rectangle class: getWidth, getHeight, __str__.
Add a method area to the Rectangle class that returns the area of any instance:
Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:
Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:
Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2). These tests should pass:
Write a new method called diagonal that will return the length of the diagonal that runs from the lower left corner to the opposite corner.
"""

class Point:
    """This represents the location of the point"""
    def __init__(self, intX, intY):
        """This is used to initialize the values"""
        self.x = intX
        self.y = intY

    def getX(self):
        """Returns the X value"""
        return self.x

    def getY(self):
        """Returns the Y Value"""
        return self.y

    def __str__(self):
        """This represents the point in the string format"""
        return "("+str(self.getX())+","+str(self.getY())+")"

class Rectangle:
    """This represents the Rectangle"""
    def __init__(self, location, intWidth, intHeight):
        """This initializes the values"""
        self.location = location
        self.width = intWidth
        self.height = intHeight

    def getWidth(self):
        """This returns the width of the rectangle"""
        return self.width

    def getHeight(self):
        """This returns the height of the rectangle"""
        return self.height

    def area(self):
        """This returns the area of the rectangle"""
        return self.getWidth()*self.getHeight()

    def perimeter(self):
        """This provides the perimeter of the rectangle"""
        return 2*(self.getWidth()+self.getHeight())

    def transpose(self):
        """This is used to interchange width and height"""
        interchange = self.getWidth()
        self.width = self.getHeight()
        self.height = interchange

    def contains(self, location2):
        """Checks whether a given point is inside the rectangle or not"""
        if location2.getX() < self.getWidth() and location2.getX()>=0:
            self.x_verify = True
        else:
            self.x_verify = False
        if location2.getY() < self.getHeight()  and location2.getY() >=0:
            self.y_verify = True
        else:
            self.x_verify = False
        if self.x_verify and self.y_verify:
            return True
        else:
            return False

    def diagonal(self):
        """This is used to provide the diagonal of the rectangle"""
        return (self.getWidth()**2+self.getHeight()**2)**0.5


    def __str__(self):
        """This represents the rectangle on the string format"""
        return "("+str(self.location)+","+str(self.getWidth())+","+str(self.getHeight())+")"

r = Rectangle(Point(3,4),8, 10)
print(r)
r2 = Rectangle(Point(0,0),10,5)
print(r2.area())
assert r2.area(),50
print('Area is asserted')
assert r2.perimeter(),30
print('Perimeter is asserted')
r2.transpose()
assert r2.width == 5
assert r2.height == 10
print('Sides are asserted')

r3 = Rectangle(Point(0, 0), 10, 5)
print(r3.contains(Point(0,0)))
print(r3.contains(Point(3,3)))
print(r3.contains(Point(3,7)))
print(r3.contains(Point(3,5)))
print(r3.contains(Point(3,4.99999)))
print(r3.contains(Point(-3,-3)))
print(r3.diagonal())
