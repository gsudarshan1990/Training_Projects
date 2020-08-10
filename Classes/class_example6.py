"""This is an example of class which initializes twice"""

class Person:
    """This class describes about the person"""
    def __init__(self):
        """This is used to intialize the values"""
        self.firstname = "Johny"
        self.lastname = "Depp"
        self.eyecolor = "grey"
        self.age = 42

person1 = Person()
person2 = Person()

person1.name = "David"
person2.name = "James"
print("Person 1 name",person1.name)
print("Person 2 name",person2.name)