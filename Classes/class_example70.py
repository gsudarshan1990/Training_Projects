#Instance variables of a class is represented in the form of dictionary


class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname):
        """This is used to initialize thev values"""
        self.firstname = firstname
        self.lastname = lastname

student = Student('rahul','bose')
print(student.__dict__)