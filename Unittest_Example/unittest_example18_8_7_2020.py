"""
This is an example of the unittest of string methods
"""

import unittest

class TestStringMethods(unittest.TestCase):
    """This is used to test certain string methods"""
    def test_upper(self):
        """This is used to test the upper methods"""
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        """This is used to test the isupper methods"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split_method(self):
        """This is used to split the methods"""
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
