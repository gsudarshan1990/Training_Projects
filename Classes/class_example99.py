#This python page describes about the property in a more elaborated way


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
        '''This is used to return the name'''
        print('This is used to return the name')
        return self.__name

    def del_name(self):
        '''This is used to delete the name'''
        del self.__name

student = Student()
student.name ='rahul'
print(student.name)
del student.name

