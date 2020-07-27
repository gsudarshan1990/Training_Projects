"""
This is an advanced example of the closure
"""

def enroll_student_college(college_name):
    """
    This is used to enroll the students in the college specific to each college name
    :param college_name: name of the college
    :return: function object
    """
    student_list = []
    def enroll_student(student_name):
        """
        This is used to enroll the student to the college
        :return: Nothing
        """
        student_list.append(student_name)
        print('Student',student_name,'has been enrolled to college', college_name)
        print(student_list)

    return enroll_student

enroll_yale_college = enroll_student_college('Yale')
enroll_yale_college('Sam')

enroll_duke_college = enroll_student_college('Duke')
enroll_duke_college('Jim')
enroll_duke_college('James')
enroll_duke_college('Johnathan')
enroll_duke_college('Watson')

enroll_yale_college('Augustan')
enroll_yale_college('Donal')
enroll_yale_college('Vicky')