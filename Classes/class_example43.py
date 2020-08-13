#This is another example of class with inheritance and method overriding


class Fruit:
    """This is used to describe the fruit"""
    def __init__(self):
        print('I am a fruit')

    def nutrition(self):
        print("I am full of nutrients")

    def cultivation(self):
        print('Every fruits get cultivated in different regions')

    def fruit_shape(self):
        print('Every fruit has different shape and some are shapeless')

class Orange(Fruit):
    """This describes the orange which is a type of fruit and forms the is a relationship with the above class"""
    def __init__(self):
        Fruit.__init__(self)
        print('My type is orange')

    def nutrition(self):
        super(Orange,self).nutrition()
        print('I contain vitamin c')

    def color(self):
        print('Apart from the name my color is also orange')

f = Fruit()
f.nutrition()
f.cultivation()
f.fruit_shape()

print('*'*20)

o = Orange()
o.nutrition()
o.cultivation()
o.fruit_shape()
o.color()