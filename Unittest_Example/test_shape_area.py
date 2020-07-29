"""
This is another example of the unittest which tests individual test cases
"""

import unittest
from Unittest_Example import shape_area


class Testing(unittest.TestCase):
    """
    This class is used to test the function of the shape_area
    """
    def test_triangle(self):
        result = shape_area.triangle_area(10,5)
        self.assertEqual(result,25)

    def test_rectangle(self):
        result = shape_area.rectangle_area(10,5)
        self.assertEqual(result,50)

    def test_square(self):
        result = shape_area.square_area(6)
        self.assertEqual(result,36)

if __name__ =='__main__':
    unittest.main()