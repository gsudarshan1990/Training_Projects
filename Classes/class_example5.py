"""
This is an example of utilization of the two classes

"""

class Name:
    """This class describes about the name of the person"""
    def __init__(self):
        """This is used to initilize the values"""
        self.firstname = "John"
        self.lastname = "Depp"

class Person:
    """This class describes about the Person"""
    def __init__(self):
        """This is used to initalize the values"""
        self.name = Name()
        self.eyecolor = 'grey'
        self.age = 42

person = Person()
print(person.name.firstname)
person.name.firstname = "David"
print(person.name.firstname)