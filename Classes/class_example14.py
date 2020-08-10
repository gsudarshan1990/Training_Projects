"""
This is an example of the class which uses the instance as the arguments
"""

class Name:
    """This elaborates about the name of the person"""
    def __init__(self, firstname, lastname):
        """This is used for initializing the values"""
        self.firstname = firstname
        self.lastname = lastname


class Person:
    """This elaborates about the person"""
    def __init__(self, name, eyecolor, age):
        """This is used for initializing the value"""
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

def capitialize(name1):
    name1.firstname = name1.firstname.upper()
    name1.lastname = name1.lastname.upper()

person1 = Person(Name("David","Robert"),"blue",42)
capitialize(person1.name)
print(person1.name.firstname)
print(person1.name.lastname)