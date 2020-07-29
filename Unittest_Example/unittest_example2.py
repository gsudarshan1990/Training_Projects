"""
This is an example of unittest with multiple tests
"""

import unittest

class Testing(unittest.TestCase):
    """
    This is a class which used for the multiple tests
    """
    def test_upper(self):
        """
        This is used to test the string is upper or not
        :return:
        """
        self.assertEqual('Beta'.upper(),'BETA')

    def test_boolean(self):
        x = True
        y = True
        self.assertEqual(x,y)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('Beta'.isupper())

if __name__ =='__main__':
    unittest.main()