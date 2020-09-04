#This is python program in classes

class Dog:
    '''This class describes about the dog'''
    def __init__(self, name, age):
        '''This is used to initialize the values'''
        self.name = name
        self.age = age

    def sit(self):
        '''This describes about the sitting of dog'''
        print(f"{self.name} is sitting")

    def roll_over(self):
        '''This describes about rollover of the dog'''
        print(f"{self.name} is rolling over")

d1 = Dog('oba',4)
d1.sit()
d1.roll_over()
print(d1.__dict__)
print(d1.__class__)
print(type(d1))
print(type(Dog))
print(isinstance(d1,Dog))