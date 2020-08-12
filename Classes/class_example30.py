"""
This is an example of the class which uses setter and getter methods and also the type error
"""

class Student:
    """This is used to describe the Student"""
    def __init__(self, studentname, enrolled):
        """This is used to initialize the values"""
        self.studentname = studentname
        self.enrolled = enrolled
        self.GPA = 0.0
        self.credithours = 0
        self.classes = []

    def getGPA(self):
        """This provides the Current GPA"""
        return self.GPA

    def setGPA(self, newGPA):
        """This is used to set the gpa"""
        print('This sets the GPA from ',self.GPA,"to",newGPA)
        self.GPA = newGPA

    def updateGPA(self, newhours, newgrades):
        newTotal = newgrades*newhours+ self.GPA*self.credithours
        self.credithours+=newhours
        self.GPA = newTotal/self.credithours

newStudent = Student('Milo', True)
#newStudent = Student() - causing the type error
newStudent.setGPA(3.5)
print(newStudent.getGPA())
