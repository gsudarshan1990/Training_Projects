#This is another python program which describes


class Student:
    '''This class describes about student'''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.mail =self.firstname+"."+self.lastname+"@xyz.com"

    def fullname(self):
        print("{} {}".format(self.firstname,self.lastname))

    def uppercase(self):
        self.firstname = self.firstname.upper()
        self.lastname = self.lastname.upper()
    
s1 = Student('Roger','Federer')
s1.uppercase()
s1.fullname()

s2 = Student('Anthony','Hopkins')
s2.uppercase()
s2.fullname()