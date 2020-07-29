"""
This is an example of the unittest which makes use of the makesuite
"""

import unittest

class TestMultiplication(unittest.TestCase):
    """
    This is an example of Multiplication Test Case
    """
    def runTest(self):
        self.assertEqual((3*5),15)

class TestAddition(unittest.TestCase):
    """
    This is an example of Addition Test Case
    """
    def runTest(self):
        self.assertEqual((1+5),6)

class TestDivision(unittest.TestCase):
    """
    This is an example of Division Test Case
    """
    def runTest(self):
        self.assertEqual((7/7),1)

class SimpleTest(unittest.TestCase):
    """
    This is a Test with 4 different test cases
    """
    def test_1(self):
        self.assertEqual(1,1)

    def test_2(self):
        self.assertEqual(2,2)

    def test_3(self):
        self.assertEqual(3,3)

    def test_4(self):
        self.assertEqual(4,4)

if __name__ == '__main__':
    suite = unittest.makeSuite(SimpleTest,'test')
    result = unittest.TextTestRunner().run(suite)
    print('\n errors ',result.errors)
    print('\n failures ',result.failures)
    print('\n successful',result.wasSuccessful())
    print('\n skipped', result.skipped)
    print('\n Total tests', result.testsRun)