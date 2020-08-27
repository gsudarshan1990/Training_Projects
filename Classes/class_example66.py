#This is another example of the class

class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        """This represents the object in the string format"""
        return f"Student({self.firstname},{self.lastname})"

    def __str__(self):
        """This provides the object in the string format"""
        return f"Student : {self.firstname} {self.lastname}"

student = Student('rahul','kanna')
print(str(student))
print(repr(student))