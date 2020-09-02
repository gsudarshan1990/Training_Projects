#This python program describes about the member functions



class Student:
    '''This class describes about the student'''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.mail=self.firstname+"."+self.lastname+"@xyz.com"

    def fullname(self):
        print('{} {}'.format(self.firstname,self.lastname))

s1 = Student('roger','federer')

s1.fullname()

print(s1.fullname)

s2 = Student('Anthony','Hopkins')
s2.fullname()

Student.fullname(s1)
Student.fullname(s2)

s3 = Student('John','Miller')
print(s3.firstname)
print(s3.lastname)

del s3.firstname

