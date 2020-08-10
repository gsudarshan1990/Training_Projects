"""
This page performs the unittest for the calculator3.py
"""

import unittest
from Unittest_Example.unittestclass.calculator3 import Calculator

class CalculatorUnittest(unittest.TestCase):
    """This performs different types of the calculator tests"""

    @classmethod
    def setUpClass(cls):
        global calc
        calc = Calculator()

    def setUp(self):
        """This performs the setup"""
        print('\n Set Up')

    def test_case_01(self):
        """This is used to perform the tests"""
        self.assertEqual(calc.add1(2,2),4)

    def test_case_02(self):
        self.assertEqual(calc.add2(2,4),6)

    def test_case_03(self):
        self.assertRaises(ValueError,calc.add1, 2,'two')

    def test_case_04(self):
        self.assertRaises(ValueError, calc.add2 , 2, 'two')


    def tearDown(self):
        print('\n Tear Down')

    @classmethod
    def tearDownClass(cls):
        del calc

if __name__ == '__main__':
    unittest.main()