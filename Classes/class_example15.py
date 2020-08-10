"""
This is an example of the class which elaborates on the actual copy
"""

class Name:
    """This describes about the name of the person"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firtname = firstname
        self.lastname = lastname


class Person:
    """This describes about the Person"""
    def __init__(self, name, eyecolor, age):
        """This is used to initialize the values"""
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

person1 = Person(Name("David","Robert"),'blue',42)
person2 = Person(person1.name,person1.eyecolor,person1.age)
person2.eyecolor = 'brown'
print(person1.eyecolor)
print(person2.eyecolor)
person2.name.firstname = "John"
print(person2.name.firstname)
print(person1.name.firstname)