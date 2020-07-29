"""
This represents the unittest which needs to be skipped
"""

import unittest
from Unittest_Example import rectangle_perimeter

class Testing(unittest.TestCase):
    """
    This class represents the test case which can be skipped
    """
    def test_equal(self):
        self.assertEqual(rectangle_perimeter.get_perimeter_rectangle(10,5),30)

    @unittest.skip('This test is temporarily skipped')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter_rectangle(10,0)

if __name__ == '__main__':
    unittest.main()