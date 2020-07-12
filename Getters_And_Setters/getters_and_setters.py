"""
This is the example of getters and setters
"""

class Student:
    """
    This class describes about the student
    """
    def __init__(self, name , classroom, student_number):
        """
        Initializes the values
        :param name: arg1 and string
        :param classroom: arg2 and string
        :param student_number: arg3 and student_number
        """
        self._name = name
        self._classroom = classroom
        self._student_number = student_number

    def getName(self):
        return self._name

    def setName(self, new_name):
        self._name=new_name

    def getClassRoom(self):
        return self._classroom

    def setClassRoom(self, new_class_room):
        self._classroom = new_class_room

    def getStudentNumber(self):
        return self._student_number

    def setStudentNumber(self, new_student_number):
        self._student_number = new_student_number

s1 = Student("Rakesh","ComputerScience",12002)
print(s1.getName())
print(s1.getStudentNumber())
print(s1.getClassRoom())
s1.setClassRoom("Biology")
print(s1.getClassRoom())