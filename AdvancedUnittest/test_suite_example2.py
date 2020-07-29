"""
This is another example of the test suite based on the Mathematics
"""

import unittest

class TestMultiplication(unittest.TestCase):
    """
    This class is used to test the multiplication
    """
    def runTest(self):
        self.assertEqual((3*5),15)

class TestAddition(unittest.TestCase):
    """
    This class is used to test the addition
    """
    def runTest(self):
        self.assertEqual((1+5),6)

class TestDivision(unittest.TestCase):
    """
    This class is used to test the Division
    """
    def runTest(self):
        self.assertEqual((7/7),1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMultiplication())
    suite.addTests([TestAddition(),TestDivision()])
    unittest.TestRunner().run(suite)
