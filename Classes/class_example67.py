#This is another example of the class


class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

    def begin_study(self):
        """This is used to begin the studying"""
        print(f"{self.firstname} {self.lastname} begins the study")

    @classmethod
    def name(cls, name_info):
        firstname = name_info['firstname']
        lastname = name_info['lastname']
        return cls(firstname, lastname)

    @staticmethod
    def work():
        return "study, eat , love"

student = Student('rahul', 'bose')
dict1 = {'firstname':'rajesh',"lastname":'kalyan'}
secondstudent = Student.name(dict1)
