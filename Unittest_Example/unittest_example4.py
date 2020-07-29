"""
This is used to test the functions defined on the areas
"""

import unittest
from Unittest_Example import areas

class Testing(unittest.TestCase):
    """
    This class tests the function defined on the area
    """
    def test_triangle(self):
        result = areas.triangle_area(10,5)
        self.assertEqual(25,result)

    def test_rectangle(self):
        result = areas.rectangle_area(10,5)
        self.assertEqual(50,result)

if __name__ =='__main__':
    unittest.main()