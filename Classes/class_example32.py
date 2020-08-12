"""
This is an example of the class and elaborating how to create the objects
"""

class Name:
    """This class provides the name with firstname and lastname"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname  = lastname

class Student:
    """This class describes the name of the student"""
    def __init__(self, studentname, enrolled):
        """This is used to initialize the Student class"""
        self.studentname = studentname
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = enrolled
        self.classes = []

newStudent = Student(Name('sonu','Garim'),True )
name1 = Name('shashank', 'Graim')
newStudent2 = Student(name1,True)
newStudent3 = Student("Sonu Garim",True)