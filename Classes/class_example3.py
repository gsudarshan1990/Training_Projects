"""This is another example of the class"""

class Person:
    """This class defines the name of the person"""
    def __init__(self):
        """This is used to initialize the values"""
        self.firstname = "John"
        self.lastname = 'Depp'
        self.eyecolor = 'black'
        self.age = 42

person = Person()
print(person.firstname)
print(person.lastname)
print(person.eyecolor)
print(person.age)