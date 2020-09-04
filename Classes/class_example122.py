#This is another python example

class Dog:
    '''This class describes about the Dog'''
    __species ='canine'

    def __init__(self, name, breed):
        '''This is used to initialize the values'''
        self.__name = name
        self.__breed = breed
        self.__tricks =[]

    def get_name(self):
        return self.__name

    def set_name(self, newname):
        self.__name = newname

    def get_breed(self):
        return self.__breed

    def set_breed(self, newbreed):
        self.__breed = newbreed

    def add_tricks(self, newtrick):
        self.__tricks.append(newtrick)

    def print_details(self):
        print('Dog name', self.__name)
        print('Dog breed',self.__breed)
        print('Dog tricks',self.__tricks)

d1 = Dog('Moje','Golden Retriver')
d1.print_details()

d1.add_tricks('roll over')
d1.print_details()

d1.set_name('oba')
d1.print_details()

d1.set_breed('labarador')
d1.print_details()