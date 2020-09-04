#This is another python program


class Shape:
    '''This class describes about the shape'''
    def __init__(self, shape_type, color ='Red'):
        self.shape_type = shape_type
        self.color = color

    def get_type(self):
        return self.shape_type

    def get_color(self):
        return self.color

circle = Shape('circle')
print(circle.get_color())

square = Shape('square','blue')
print(square.get_color())