"""
This is an example of unittest case
"""

import unittest

class Testing(unittest.TestCase):
    """
    This class is used to test the string
    """
    def test_string(self):
        self.x ='alpha'
        self.y ='alpha'
        self.assertEqual(self.x,self.y)

if __name__ =='__main__':
    unittest.main()