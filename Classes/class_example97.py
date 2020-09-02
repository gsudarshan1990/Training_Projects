#This is a python example with the private attribute


class Student:
    """This class describes about the student"""
    def __init__(self):
        """This is used to initialize the values"""
        self.__name = ''

    def set_name(self, name):
        """This is used to set the name"""
        print('Setter method is called')
        self.__name = name

    def get_name(self):
        """This is used to return the name"""
        print('Getter method is called')
        return self.__name

student= Student()

student.set_name('rahul')
print(student.get_name())

print(student.__dict__)
print(student._Student__name)