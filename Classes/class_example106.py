#This python program is about static method


class Rectangle:

    def area(length, breadth):
        return length*breadth

Rectangle.area=staticmethod(Rectangle.area)

print(Rectangle.area(10,12))

class Square:

    def area(side):
        return side**2

    area=staticmethod(area)

print(Square.area(7))