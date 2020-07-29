"""
This is used to test the functions on area in another method
"""

import unittest
from Unittest_Example import areas

class Testing(unittest.TestCase):
    """
    This is used to test area of the triangle
    """
    def runTest(self):
        result = areas.triangle_area(10,5)
        self.assertEqual(25,result)

if __name__ == '__main__':
    unittest.main()