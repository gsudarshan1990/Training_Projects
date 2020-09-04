"""This is another python example"""

class Product:
    def __new__(cls, *args, **kwargs):
        new_product = object.__new__(cls)
        print('Product __new__ is called')
        return new_product

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print('__init__ is called')

p1 = Product('vaccum', 150)