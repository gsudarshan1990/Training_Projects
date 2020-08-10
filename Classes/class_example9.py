"""
This class describes about the default parameters for constructors
"""

class Person:
    """This class is used to describe about the Person"""
    def __init__(self, firstname ="Johnathan", lastname="Robert"):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = 'grey'
        self.age = 42

person = Person()
print(person.firstname,person.lastname)
person2 = Person(firstname = "David")
print(person2.firstname, person2.lastname)
person3 = Person("Teesta")
print(person3.firstname,person3.lastname)
