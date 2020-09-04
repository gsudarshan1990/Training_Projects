#This is another python program


class Dog:
    '''This class describes about the dog'''
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    def print_details(self):
        print('The name of the dog is %s and breed is %s'%(self.__name, self.__breed))

    def change_name(self, name):
        self.__name = name

d1 = Dog('Nemo', 'Golden Retriever')
d1.print_details()
d1.change_name('oba')
d1.print_details()
        