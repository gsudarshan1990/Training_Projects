#This is another python example with the property decorator

class Wrestler:
    '''This class describes about the wrestlers'''
    def __init__(self):
        self.__name = ''
        self.__age = None

    @property
    def name(self):
        '''This is used to return'''
        print('getter is called')
        return self.__name

    @name.setter
    def name(self, newname):
        '''This is used to set the name'''
        print('setter is called')
        self.__name = newname

    @name.deleter
    def name(self):
        '''This is used to delete the name'''
        print('Deletion of the name is performed')
        del self.__name

    @property
    def age(self):
        '''This is used to return the age'''
        print('Setter method is called')
        return self.__age

    @age.setter
    def age(self, newage ):
        '''This is used to set the age'''
        print('Getter method is called')
        self.__age = newage

    @age.deleter
    def age(self):
        '''This is used to delete the age'''
        print('Delete action is performed')
        self.__age = None

wrestler = Wrestler()
wrestler.name='John'
wrestler.age ='29'
print(wrestler.name)
print(wrestler.age)
