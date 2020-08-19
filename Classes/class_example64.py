"""
The below class implements raise NotImplementError
"""

class Fruit:
    def taste(self):
        raise NotImplementedError()

    def originated(self):
        raise NotImplementedError()

class Apple:
    def originated(self):
        return "Central Asia"

f= Fruit()
#f.originated()