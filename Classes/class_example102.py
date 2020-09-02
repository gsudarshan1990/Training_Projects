#This python pages describes about the inheritance


class Hominidae():

    def diet(self):
        pass

    def walk(self):
        pass

    def behavior(self):
        print('This show complex facial expression and social behavior')

chimpanzee = Hominidae()
chimpanzee.behavior()
chimpanzee.walk()
chimpanzee.diet()

class Humans(Hominidae):
    '''This class inherits the Hominidae'''
    def diet(self):
        print('Humans are ominivores')

    def walk(self):
        print('They walk bipeds')

paul= Humans()
paul.diet()
paul.walk()