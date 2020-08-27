#This is another example of the class

class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

    @property
    def name(self):
        print('Get the name')
        return f"{self.firstname} {self.lastname}"

    @name.setter
    def name(self, name):
        print('This is used to set the name')
        self.firstname, self.lastname = name.split()

s1 = Student('Rakesh','Kanna')
print(s1.name)
s1.name = 'rahul bose'
print(s1.name)
