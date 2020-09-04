#This is another python example


class Dog:
    '''This class describes about the dog'''
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def print_details(self):
        '''This class prints the details'''
        print('The name of the dog %s and breed is %s'%(self.name, self.breed))


d1 = Dog('oba','Labarador')
d1.print_details()

print(d1.__dict__)
d1.name = 'Nemo'
d1.print_details()
d1. breed ='Golden Retriever'

d1.print_details()
print(d1.__dict__)