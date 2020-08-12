"""
This is used to describe the co-ordinate in the graph along with the dunder methods
"""

class Co_ordinate:
    """This class represents the point on the graph"""
    total_objects = []
    def __init__(self, x, y):
        """This is used to initialize the values"""
        self.x = x
        self.y = y
        Co_ordinate.total_objects.append(self)



    def distance_from_origin(self):
        """This function provides the distance from origin"""
        x_dist = self.x**2
        y_dist = self.y**2
        return (x_dist+y_dist)**2

    def __str__(self):
        """This is used to represent the co-ordinate on the string formation"""
        return "("+str(self.x)+","+str(self.y)+")"

    def __repr__(self):
        """This is used to represent the co-ordinate on the class format"""
        return "Co-ordinate("+str(self.x)+","+str(self.y)+")"

    def __add__(self, other):
        """This is used to add two co-ordinates"""
        self.new_x = self.x+other.x
        self.new_y = self.y+other.y
        return Co_ordinate(self.new_x,self.new_y)

    def __sub__(self, other):
        """This is used to subtract two co-ordinates"""
        self.new_x = self.x - other.x
        self.new_y = self.y - other.y
        return Co_ordinate(self.new_x,self.new_y)

    def __eq__(self, other):
        """This is used to check whether two points are same"""
        value = (self.x == other.x) and (self.y == other.y)
        return value

    def gradient(self, other):
        """This is used to find the slope between two points"""
        return (other.y - self.y)/(other.x -self.x)

    def distance_between_two_points(self, other):
        """This is used to find the distance between two points"""
        self.dist_x = (self.x - other.x)**2
        self.dist_y = (self.y - other.y)**2
        return (self.dist_x + self.dist_y)**2

    def __len__(self):
        """This defines the total number of objects created"""
        return len(Co_ordinate.total_objects)

c = Co_ordinate(3,4)
d = Co_ordinate(5,6)
print(c)
print(repr(c))
print(c.distance_from_origin())
print(c+d)
print(c-d)
print(repr(c+d))
print(repr(c-d))
print(c.distance_between_two_points(d))
e = Co_ordinate(3,4)
print(c == e)
print(len(e))