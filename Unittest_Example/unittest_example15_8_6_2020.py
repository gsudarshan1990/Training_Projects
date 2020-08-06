"""This is another example of the unittest describing about the test"""


import unittest


class UnittestDescription(unittest.TestCase):
    """This class describest the test"""

    def test_description(self):
        """This function provides the information about the test earlier"""
        print('\n About the test')
        print(self.id())
        print(self.shortDescription())

if __name__ == '__main__':
    unittest.main()
