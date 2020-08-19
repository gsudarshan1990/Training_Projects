from Classes.Inheritance_static_class_method.shape import Shape

import math
class Square(Shape):
    """This class describes about the Shape which forms the is a relationship with Shape"""
    all_squares =[]
    def __init__(self, x =0, y =0, side =2):
        """This is used to initialize the values and cummulate the squares"""
        super().__init__(x,y)
        self.side = side
        self.__class__.all_squares.append(self)

    @classmethod
    def total_area(cls):
        """This provides the total area of all the squares"""
        cummulative_area =0
        for c in cls.all_squares:
            cummulative_area+=cls.area(c.side)
        return cummulative_area

    @classmethod
    def total_perimeter(cls):
        """This provides the cummulative perimeter of all the squares"""
        cummulative_perimeter = 0
        for c in cls.all_squares:
            cummulative_perimeter+=cls.perimeter(c.side)
        return cummulative_perimeter

    @staticmethod
    def area(side1):
        return math.pow(side1,2)

    @staticmethod
    def perimeter(side1):
        return 4*side1

s1 = Square()
s2 = Square(1,2, 4)
s3 = Square(1,4, 8)
s4 = Square(2, 1, 12)

print(Square.total_perimeter())
print(Square.total_area())