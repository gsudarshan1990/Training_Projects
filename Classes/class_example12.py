"""
This is another example of the class which combines another class
"""

class Name:
    """This is used to define about the name of the Person"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname

class Person:
    """This is used to describe the class of the person"""
    def __init__(self, name, eyecolor, age):
        """This is used to initialize the values"""
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

person = Person(Name("David","Robert"),"blue",42)
print(person.name.firstname)
print(person.name.lastname)
print(person.eyecolor)
print(person.age)