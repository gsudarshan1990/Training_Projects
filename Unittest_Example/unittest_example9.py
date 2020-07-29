"""
This is another example of the unittest which uses equal asserts
"""

import unittest

class Testing(unittest.TestCase):
    """
    This class contains two functions which tests assertequal and assertnotequal
    """
    def test_equal(self):
        self.assertEqual(6,(8-2))

    def test_not_equal(self):
        self.assertNotEqual(7,(4*2))

if __name__ == '__main__':
    unittest.main()