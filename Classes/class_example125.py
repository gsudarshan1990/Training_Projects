#This is another python class example


class Shape:
    pass

class Shape():
    pass

class Shape(object):
    pass

class Shape:

    def __init__(self, shape_type):
        self.shape_type = shape_type

    def get_type(self):
        return self.shape_type

circle = Shape('Circle')
print(type(circle))


square = Shape('Square')
print(type(square))

print(square.get_type())