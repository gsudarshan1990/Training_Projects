#This is another python program


class Shape:
    '''This class describes about the shape'''
    def __init__(self, shape_type, color ='Red'):
        self.__shape_type  = shape_type
        self.__color = color

    def get_type(self):
        return self.__shape_type

    def get_color(self):
        return self.__color

    def get_parameter(self):
        pass

    def get_area(self):
        pass

class Circle(Shape):
    pass

circle = Circle('circle')

print(circle.get_color())
print(circle.get_type())

class Square(Shape):
    def __init__(self, shape_type):
        Shape.__init__(self, shape_type, color ='blue')

square= Square('square')
print(square)

print(square.get_type())
print(square.get_color())