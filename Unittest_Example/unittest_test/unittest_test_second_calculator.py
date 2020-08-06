"""
This tests the class in which the function raises the exception
"""

import unittest
from Unittest_Example.unittestclass.calculator2 import SecondCalculator

class TestSecondCalculator(unittest.TestCase):
    """This tests the calculator"""
    def setUp(self):
        """This setups the object"""
        self.scalc = SecondCalculator()

    def test_add(self):
        """This tests the add function from the second calculator"""
        self.assertEqual(self.scalc.add(2,3),5)
        self.assertEqual(self.scalc.add("h",5),10)

    def tearDown(self):
        del self.scalc

if __name__ == '__main__':
    unittest.main()