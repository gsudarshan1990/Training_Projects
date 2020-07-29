"""
This is an example of the unittest which describes another method for using the assertRaises
"""

import unittest
from Unittest_Example import rectangle_perimeter

class Testing(unittest.TestCase):
    """
    This class describes the assertRaises in different method
    """
    def test_equal(self):
        self.assertTrue(rectangle_perimeter.get_perimeter_rectangle(10,5),30)

    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter_rectangle(10,0)

if __name__ == '__main__':
    unittest.main()