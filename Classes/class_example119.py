#This is another python example


class Dog:
    '''This class describes about the Dog'''
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    def print_details(self):
        print('The name of the dog is %s and breed is %s'%(self.__name,self.__breed))

d1 = Dog('oba','labarador')
d1.print_details()
d1.__name ='nemo'
print(d1.__dict__)
d1._Dog__name ='Nemo'
d1.print_details()