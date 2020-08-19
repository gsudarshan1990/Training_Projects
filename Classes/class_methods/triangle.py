"""
This python program elaborates on the class methods
"""

class Triangle:
    """This class represents the Triangle"""
    all_triangles =[]
    def __init__(self, height, base):
        """This is used to initialize the values"""
        self.height = height
        self.base = base
        self.__class__.all_triangles.append(self)

    def area(self):
        """This function calculates the area of the triangle"""
        return (self.height*self.base)*0.5

    @classmethod
    def total_area(cls):
        """This provides total area of all the triangles"""
        cummulative_area = 0
        for t in cls.all_triangles:
            cummulative_area+=t.area()
        return cummulative_area

    def __repr__(self):
        """This represents the triangle in the string format"""
        return "Triangle("+str(self.base)+" , "+str(self.height)+")"