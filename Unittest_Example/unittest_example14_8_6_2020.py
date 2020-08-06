"""This is a sample example of the unittest"""


import unittest

class UnitTestExample(unittest.TestCase):
    """This is used for testing the class"""
    def test_case_01(self):
        my_str ='Sonu'
        my_int = 23
        self.assertTrue(isinstance(my_str,str))
        self.assertTrue(isinstance(my_int,int))

    def test_case_02(self):
        my_pi =3.14
        self.assertFalse(isinstance(my_pi,int))

if __name__ == '__main__':
    unittest.main()