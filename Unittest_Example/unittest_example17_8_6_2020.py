"""
This page explains the skipping of unittest case
"""

import unittest
import sys

class DemonstrateSkipUnitTest(unittest.TestCase):
    """This class demonstrate the unittest case"""

    @unittest.skip("Demonstrating the unconditional skip")
    def testcase_01(self):
        self.fail('Fatal')

    @unittest.skipUnless(sys.platform.startswith("win"),"Using the windows")
    def testcase_02(self):
        """Skipping the test if os is not windows"""
        print(self.id())
        print(self.shortDescription())

    @unittest.skipUnless(sys.platform.startswith("lin"),"using the linux")
    def testcase_03(self):
        pass

if __name__ == '__main__':
    unittest.main()