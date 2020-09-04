#This is python program on polymorhpism


class Hominidae:
    '''This class describes about the Hominidae'''
    def communication(self):
        print('They use the auditory calls and visual cues')

    def walk(self):
        print('They are knuckle walkers and use hang from one tree to another')

class Humans(Hominidae):
    '''This class inherits from the Hominidae and perform the polymorphism'''
    def communication(self):
        print('They use language to communicate')

    def walk(self):
        print('They are bipeds')

class Gorilla(Hominidae):
    '''This class inherits from Hominidae'''
    def communication(self):
        print('They use vocilaztions to communicate')

    def walk(self):
        print('They are knuckle walkers')

h1 = Hominidae()
h1.communication()
h1.walk()
print('*'*20)
h2 = Humans()
h1.walk()
h1.communication()
print('*'*20)
g1 = Gorilla()
g1.communication()
g1.walk()