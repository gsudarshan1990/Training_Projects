"""
This class represents another static methods
"""

class Rectangle:
    """This class describes about the rectangle"""
    all_rectangles =[]

    def __init__(self, length, breadth):
        """This is used to initialize the values and cummulate the instance"""
        self.length = length
        self.breadth = breadth
        self.__class__.all_rectangles.append(self)

    def area(self):
        """This provides the area of the rectangle"""
        return self.length*self.breadth

    def perimeter(self):
        """This provides the perimeter of the rectangle"""
        return 2*(self.length+self.breadth)

    def __len__(self):
        """This provides total rectangle instances"""
        return len(self.__class__.all_rectangles)

    @staticmethod
    def total_area():
        """This provides the total area of all the rectangles"""
        cummulative_area = 0
        for r in Rectangle.all_rectangles:
            cummulative_area+=r.area()
        return cummulative_area

    @staticmethod
    def total_perimeter():
        """This provides the total perimeter of the rectangles"""
        cummulative_perimeter = 0
        for r in Rectangle.all_rectangles:
            cummulative_perimeter+=r.perimeter()
        return cummulative_perimeter

