"""
This is an example of the unittest which uses the assert statement
"""

import unittest

class Testing(unittest.TestCase):
    """
    This is used for asserting the boolean values
    """
    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)

    def test_assert_true_with_expression(self):
        self.assertTrue((5-2) == 3)

    def test_assert_false_with_expression(self):
        self.assertFalse((5-2) == 4)

if __name__ == '__main__':
    unittest.main()