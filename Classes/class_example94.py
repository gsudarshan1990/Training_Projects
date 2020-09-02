#This python file describes about the len function


class Student:
    """This class describes about the student"""
    def __init__(self):
        """This is used to initialize the values"""
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def __len__(self):
        return len(self.__students)

student = Student()
student.add_student('rahul')
student.add_student('Johnathan')
student.add_student('sonu')
print(len(student))