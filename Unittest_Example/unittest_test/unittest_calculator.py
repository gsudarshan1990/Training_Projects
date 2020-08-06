"""
This tests the calculator class
"""

import unittest
from Unittest_Example.unittestclass.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """This class tests the Calculator class"""
    def setUp(self):
        self.calc = Calculator()

    def test_add_method(self):
        """Test the functions"""
        self.assertEqual(self.calc.add(2,3),5)
        self.assertNotEqual(self.calc.add(2,5),6)

    def tearDown(self):
        del self.calc

if __name__ == '__main__':
    unittest.main()