#This is another python program


class Dog:
    '''This class describes about the dog'''
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
        self.__tricks = []

    def print_details(self):
        '''This class prints the details about the dog'''
        print('The name of the dog is %s and breed is %s and tricks %s'%(self.__name, self.__breed, self.__tricks))

    def change_name(self, newname):
        print('Changing the name')
        self.__name = newname

    def change_breed(self, newbreed):
        print('Changing the new breed')
        self.__breed = newbreed

    def change_name_and_breed(self, name, breed):
        self.__name = name
        self.__breed = breed

d1 = Dog('ola','Golden Retriever')
d1.print_details()
d1.change_name_and_breed('nemo','labrador')
d1.print_details()