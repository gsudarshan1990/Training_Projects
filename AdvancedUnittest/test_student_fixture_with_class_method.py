"""
This is an example of the unittest case which tests the student class with the advanced class methods
"""

import unittest
from AdvancedUnittest.student import Student

class Testing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SetUp Class')

    @classmethod
    def tearDownClass(cls):
        print('tear Down Class')

    def setUp(self):
        print('\n SetUp ')
        self.stu_1 = Student('Robin','Wills',25000)
        self.stu_2 = Student('Mark','Smith',28000)

    def tearDown(self):
        print('\n teardown')

    def test_mail(self):
        print('\n test mail')
        self.assertEqual(self.stu_1.mail,'Robin.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail,'Mark.Smith@xyz.com')

        self.stu_1.first ='Jennifer'
        self.stu_2.first = 'Graham'

        self.assertEqual(self.stu_1.mail,'Jennifer.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail,'Graham.Smith@xyz.com')

    def test_fullname(self):
        print('\n test full name')
        self.assertEqual(self.stu_1.fullname,'Robin Wills')
        self.assertEqual(self.stu_2.fullname,'Mark Smith')

        self.stu_1.first ='Jennifer'
        self.stu_2.first = 'Graham'

        self.assertEqual(self.stu_1.fullname,'Jennifer Wills')
        self.assertEqual(self.stu_2.fullname,'Graham Smith')

    def test_hike_rate(self):
        print('\n test hike rate')
        self.stu_1.apply_hike_rate()
        self.stu_2.apply_hike_rate()

        self.assertEqual(self.stu_1.stipend,26250)
        self.assertEqual(self.stu_2.stipend,29400)

if __name__ == '__main__':
    unittest.main()