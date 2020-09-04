#This is another example of the unittest


class TexttheString:
    def lower_strip_the_string(self, str):
        result = str.lower().strip()
        return result

import unittest

class TestTexttheString(unittest.TestCase):
    def test_lower_strip_the_string(self):
        c = TexttheString()
        string1 ='    SOME TEXT   '
        result2 =c.lower_strip_the_string(string1)
        self.assertEqual(result2,'some text')

if __name__ == '__main__':
    unittest.main()