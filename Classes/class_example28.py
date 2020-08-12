"""
This is another example of the class and exhibiting the type error when no initial values is provided
"""

class Student:
    """This class describes about the student arguments at parameter"""
    def __init__(self, studentname, enrolled):
        """This is used to initialize the values"""
        self.studentname = studentname
        self.GPA = 0.0
        self.credithours = 0
        self.enrolled = enrolled
        self.classes = []

newStudent = Student("Milo",False)
#newStudent1 = Student()