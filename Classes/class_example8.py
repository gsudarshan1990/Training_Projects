"""
This is an example of the class with the constructors
"""

class Person:
    """This class describes about the person"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = 'grey'
        self.age = 42

person = Person("James","Watt")
print(person.firstname)
print(person.lastname)

#person2 = Person()

