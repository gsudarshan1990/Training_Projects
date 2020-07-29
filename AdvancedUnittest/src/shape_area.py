"""
This is another method of utilizing the Pycharm Unittest
"""

class ShapeArea:
    """
    This class provides area for three different polygons
    """
    @staticmethod
    def triangle_area(height,base):
        """
        This provides area of the triangle
        :param height: arg1 and is height of the triangle
        :param base: arg2 and is base of the triangle
        :return: area of the triangle
        """
        return 0.5*height*base

    @staticmethod
    def square_area(side):
             """
             This provides area of the square
             :param side: arg1 and is side of the square
             :return: area of the square
             """
             return side**2

    @staticmethod
    def rectangle_area(length,breadth):
        """
        This provides area of the rectangle
        :param length: arg1 and is length of the rectangle
        :param breadth: arg2 and is breadth of the rectangle
        :return: area of the rectangle
        """
        return length*breadth