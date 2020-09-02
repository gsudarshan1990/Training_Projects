#This is another python example which elaborates on property


class Student:
    """This class describes about the student"""
    def __init__(self):
        """This is used to initialize the values"""
        self.__name = ''

    def set_name(self, name):
        '''This is used to set the name'''
        print('This is used to set the name')
        self.__name = name

    def get_name(self):
        '''This is used to get the name'''
        print('This is used to get the name')
        return self.__name

    name = property(fget=get_name, fset= set_name)

student = Student()
student.name = 'rahul'
print(student.name)