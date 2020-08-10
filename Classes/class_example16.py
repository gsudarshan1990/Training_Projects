"""
This is another example of the class when constructors takens an object we should initialize the object while present on the argument
"""

class Name:
    """This is used to describe about the name"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname


class Person:
    """This is used to describe about the person"""
    def __init__(self, name, eyecolor, age):
        """This is used to initialize the values"""
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

person1 = Person(Name("David","Robert"),'blue',42)
person2 = Person(Name(person1.name.firstname,person1.name.lastname),person1.eyecolor,person1.age)
person2.eyecolor='brown'
print(person1.eyecolor)
print(person2.eyecolor)
person2.name.firstname = "John"
print(person1.name.firstname)
print(person2.name.firstname)