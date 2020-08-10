"""
This is another example of the class
"""

class Person:
    """This class provides information related to the Person"""
    def __init__(self):
        """This is used to initialize the values"""
        self.firstname = "John"
        self.lastname = "Depp"
        self.eyecolor = "grey"
        self.age = 42

person = Person()
print(person.firstname)
person.firstname = "David"
print(person.firstname)