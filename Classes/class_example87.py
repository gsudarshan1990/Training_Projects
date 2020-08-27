#This python program is about another python class


def create_animal_class():
    '''This function creates the object of animal class'''
    class Animal:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    return Animal

a = create_animal_class()

b=a('dog')
print(b)