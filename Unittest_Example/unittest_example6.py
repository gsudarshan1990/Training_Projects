"""
This is an example of the unittest which has multiple test cases out of which one fails
"""

import unittest
from Unittest_Example import shape_area

class Testing(unittest.TestCase):
    """
    This is the class which contains the set of test cases
    """
    def test_triangle(self):
        """
        This is used to test the result obtained from the area of the triangle
        :return: nothing
        """
        result = shape_area.triangle_area(10,5)
        self.assertEqual(result,25)

    def test_rectangle(self):
        """
        This is used to test the result obtained from the area of the rectangle
        :return: nothing
        """
        result = shape_area.rectangle_area(6,7)
        self.assertEqual(result,26)

    def test_square(self):
        """
        This is used to test the result obtained from the area of the square
        :return: Nothing
        """
        result = shape_area.square_area(5)
        self.assertEqual(result,25)

if __name__ == '__main__':
    unittest.main()
