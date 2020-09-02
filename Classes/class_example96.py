#This is another example of the python class


class Student:
    """This class describes about the student"""
    def __init__(self):
        self.__students =[]
        self.index = 0

    def add_student(self, name):
        self.__students.append(name)

    def __len__(self):
        return len(self.__students)

    def __iter__(self):
        self.index =0
        return self

    def __next__(self):
        if self.index == len(self.__students):
            raise StopIteration
        s1= self.__students[self.index]
        self.index+=1
        return s1

students = Student()
students.add_student('rahul')
students.add_student('rahim')
students.add_student('sonu')

for student in students:
    print(student)

