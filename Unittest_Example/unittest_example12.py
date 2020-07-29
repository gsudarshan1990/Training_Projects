"""
This file provides about another assert values
"""

import unittest

class SampleClass:
    pass

sc = SampleClass()
sc2 = sc

class Testing(unittest.TestCase):
    """
    This class uses additional asserts like assertIs and assertIsNot
    """
    def test_assert_is(self):
        self.assertIs(sc,sc2)

    def test_assert_is_not(self):
        self.assertIsNot('beta',int)

if __name__ == '__main__':
    unittest.main()