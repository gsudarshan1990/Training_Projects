"""
This is another example of the class which uses the static methods
"""
import math
class Square:
    """This class represents the square"""
    all_squares =[]
    pow = math.pow
    def __init__(self, side):
        """This is used to initialize the values and configure total number of the squares"""
        self.side = side
        self.__class__.all_squares.append(self)

    def area(self):
        """This provides the area of the square"""
        return pow(self.side,2)

    def perimeter(self):
        """This provides the perimeter of the square"""
        return 4*self.side

    @staticmethod
    def total_area():
        """This provides the total area"""
        cummulative_area =0
        for sq in Square.all_squares:
            cummulative_area+=sq.area()
        return cummulative_area

    @staticmethod
    def total_perimeter():
        """This provides the total perimeter of all the squares"""
        cummulative_perimeter = 0
        for sq in Square.all_squares:
            cummulative_perimeter+=sq.perimeter()
        return cummulative_perimeter

    def __len__(self):
        """This returns the total number of the squares"""
        return len(self.__class__.all_squares)




