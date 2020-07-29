"""
This is an example of the unittest case which uses the test suite
"""

import unittest

class TestString(unittest.TestCase):
    """
    This is used to test the string
    """
    def test_string(self):
        self.assertEqual('a'*4,'aaaa')

class TestUCase(unittest.TestCase):
    """
    This is used to test whether the string is a upper case or not
    """
    def test_uppercase(self):
        self.assertEqual('gama'.upper(),'GAMA')

if __name__ == '__main__':
    suite = unittest.TestSuite([TestString(),TestUCase()])
    unittest.TextTestRunner().run(suite)