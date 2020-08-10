"""
This is another example of class which elaborates on instance assignments
"""

class Name:
    """This class elaborates about the name"""
    def __init__(self, firstname, lastname):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname


class Person:
    """This class eloborates about the Person"""
    def __init__(self, name, eyecolor, age):
        """This is used to initialize the values"""
        self.name = name
        self.eyecolor = eyecolor
        self.age = age


person1 = Person(Name("David","Gotham"),'brown',42)
person2 = person1
person2.eyecolor = 'blue'
print('person1-eyecolor',person1.eyecolor)
print('person2-eyecolor',person2.eyecolor)