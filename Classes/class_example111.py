#This is another example of the python program


class Student:
    '''This class describes about the student'''
    def __init__(self, name):
        self.name = name
        self.mail = self.name+"@xyz.com"

#s1 = Student()

s1 = Student('Michael')
print(s1.name)
print(s1.mail)

#s2 = Student('Michael','Michael@xyz.com')

s2 = Student('chad')
print(s2.name)
print(s2.mail)