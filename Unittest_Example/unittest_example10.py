"""
This is another example of the unittest
"""

import unittest
from Unittest_Example import rectangle_perimeter

class Testing(unittest.TestCase):
    """
    This class provides the example of the assertraises
    """
    def test_rectangle(self):
        self.assertEqual(rectangle_perimeter.get_perimeter_rectangle(10,5), 30)

   #This uses the assert raises and parameters are passed as the arguments
    def test_rectangle_error(self):
        self.assertRaises(ValueError,rectangle_perimeter.get_perimeter_rectangle,10,0)

if __name__ == '__main__':
    unittest.main()