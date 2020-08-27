

class Student:
    """This class represents the student instance variables in the dictionary form"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

class StudentSlot:
    """This class does not represent the student instance variable in the dictionary form """
    __slots__ = ['firstname', 'lastname']

    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

student = Student('rahul', 'bose')
studentslot  = StudentSlot('rajesh','kanna')
print(student.__dict__)
#print(studentslot.__dict__)