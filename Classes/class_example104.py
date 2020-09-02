#This python program describes about abstract method


from abc import ABC, abstractmethod

class Hominidae(ABC):
    '''This class describes about Hominidae'''

    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def behavior(self):
        print('They show complex facial expression and social behavior')

class Humans(Hominidae):

    def diet(self):
        print('Humans are ominivores')

    def walk(self):
        print('Humans are bipeds')

catherine = Humans()
catherine.diet()
catherine.walk()
