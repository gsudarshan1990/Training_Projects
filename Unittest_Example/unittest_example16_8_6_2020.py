"""This is used for the intentional failing of the test cases via unittest"""

import unittest


class FailUnittest(unittest.TestCase):
    """This class implements the failure of the testcase explicitly"""

    def test_exhibit_failure(self):
        """This test fails explicitly"""
        print('\n About test')
        print(self.id())
        self.fail('Failed Explicitly')

if __name__ == '__main__':
    unittest.main()