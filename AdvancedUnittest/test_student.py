"""
This is the unit test file which tests the student class
"""

import unittest
from AdvancedUnittest.student import Student

class Testing(unittest.TestCase):
    """
    This class is used to test all the features of the student class
    """
    def test_mail(self):
        """
        This is used to test the mail property of the Student class
        :return: Nothing
        """
        stu_1 = Student('Robin','Wills',25000)
        stu_2 = Student('Mark','Smith',28000)

        self.assertEqual(stu_1.mail,'Robin.Wills@xyz.com')
        self.assertEqual(stu_2.mail,'Mark.Smith@xyz.com')

        stu_1.first = 'Jennifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.mail, 'Jennifer.Wills@xyz.com')
        self.assertEqual(stu_2.mail,'Graham.Smith@xyz.com')

    def test_fullname(self):
        """
        This function tests the fullname property of the student
        :return: Nothing
        """
        stu_1 = Student('Robin','Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)

        self.assertEqual(stu_1.fullname,'Robin Wills')
        self.assertEqual(stu_2.fullname,'Mark Smith')

        stu_1.first = 'Jennifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.fullname, 'Jennifer Wills')
        self.assertEqual(stu_2.fullname,'Graham Smith')

    def test_hike(self):
        """
        This is used to test the hike property
        :return:
        """
        stu_1 = Student('Robin','Wills',25000)
        stu_2 = Student('Mark','Smith',28000)
        stu_1.apply_hike_rate()
        stu_2.apply_hike_rate()
        self.assertEqual(stu_1.stipend,26250)
        self.assertEqual(stu_2.stipend,29400)

if __name__ == '__main__':
    unittest.main()
