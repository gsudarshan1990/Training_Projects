#This is another example of the unittest



import unittest

class TesttheFunctions(unittest.TestCase):
    def testingabilitytotest(self):
        x=1
        self.assertEqual(x,1)

    def test_the_string(self):
        word ='hello world!'
        newword =word.title()
        self.assertEqual('Hello World!',newword)

if __name__ == '__main__':
    unittest.main()