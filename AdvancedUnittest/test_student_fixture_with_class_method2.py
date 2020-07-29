"""
This is another example of the unittest which uses the setUpClass and tearDownClass
"""

import unittest
from AdvancedUnittest.student import Student

class Testing(unittest.TestCase):
    """
    This is class uses the class methods
    """
    @classmethod
    def setUpClass(cls):
        print('\n Set Up Class ')
        cls.stu_1 = Student('Robin','Wills',25000)
        cls.stu_2 = Student('Mark','Smith',28000)

    @classmethod
    def tearDownClass(cls):
        print('\n Tear Down Class')

    def setUp(self):
        print('set Up')

    def tearDown(self):
        print('tear Down')

    def test_mail(self):
        print('test Mail')
        self.assertEqual(self.stu_1.mail,'Robin.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail,'Mark.Smith@xyz.com')

    def test_fullname(self):
        print('test full Name')
        self.assertEqual(self.stu_1.fullname,'Robin Wills')
        self.assertEqual(self.stu_2.fullname,'Mark Smith')

    def test_hike_rate(self):
        print('test hike')
        self.stu_1.apply_hike_rate()
        self.stu_2.apply_hike_rate()

        self.assertEqual(self.stu_1.stipend,26250)
        self.assertEqual(self.stu_2.stipend,29400)

if __name__ == '__main__':
    unittest.main()