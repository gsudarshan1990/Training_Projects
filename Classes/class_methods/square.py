"""
This python program elaborates on the class method
"""

class Square:
    """This class describes about the Square"""
    all_squares = []

    def __init__(self, side):
        """This is used to initialize the values"""
        self.side = side
        self.__class__.all_squares.append(self)

    def area(self):
        """This provides the area of the square"""
        return self.side**2

    def perimeter(self):
        """This provides the perimeter of the square"""
        return 4*self.side

    @classmethod
    def total_area(cls):
        """This provides the total area of all the circles"""
        cummulative_area = 0
        for s in cls.all_squares:
            cummulative_area+=s.area()
        return cummulative_area

    @classmethod
    def total_perimeter(cls):
        """This provides the total perimeter of"""
        cummulative_perimeter = 0
        for s in cls.all_squares:
            cummulative_perimeter+=s.perimeter()
        return cummulative_perimeter


