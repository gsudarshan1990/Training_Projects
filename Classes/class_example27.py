"""
This is another example of the class which is
"""

class Student:
    """This class represents the Student"""
    def __init__(self):
        """This is used to initialize the values"""
        self.student = ""
        self.GPA = 0.0
        self.credithours = 0
        self.enrolled = True
        self.classes = []

newStudent =Student()
newStudent.name = 'Sonu'
newStudent.GPA = 3.9
newStudent.credithours = 40
newStudent.enrolled = True
newStudent.classes = ["Maths","Physics","Chemistry"]