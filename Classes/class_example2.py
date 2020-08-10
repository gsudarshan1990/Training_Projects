"""
This is another example of the class
"""

class Name:
    """This class defines the name of the person"""
    def __init__(self):
        """This initializes the values"""
        self.firstname = "Johnny"
        self.lastname = "Depp"

class Person:
    """This class is used to define the Person"""
    def __init__(self):
        """This is used to initialize the values"""
        self.name = Name()
        self.eyecolor = 'grey'
        self.age = 49
