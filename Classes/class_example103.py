#This python program describes about absract class


from abc import ABC

class Hominidae(ABC):
    '''This class describes about the Hominidae'''
    def diet(self):
        pass

    def walk(self):
        pass

    def behavior(self):
        print('They show complex facial expression and social behavior')

chimpanzee = Hominidae()
chimpanzee.behavior()
chimpanzee.walk()
chimpanzee.diet()

class Humans(Hominidae):

    def diet(self):
        print('Humans are ominivores')

    def walk(self):
        print('They are bipeds')

mary = Humans()
mary.walk()
mary.diet()