"""
This is another example of the unittest case with a failed test case
"""

import unittest

class Testing(unittest.TestCase):
    """
    This is the class which inherits Test Case and which defines the function in the form of test cases
    """
    def test_string(self):
        """
        Test the string
        :return:
        """
        self.assertEqual('beta'.upper(),'BETA')

    def test_boolean(self):
        """
        Testing the boolean
        :return:
        """
        x =True
        y = False
        self.assertEqual(x,y)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('beta'.isupper())

if __name__ =='__main__':
    unittest.main()