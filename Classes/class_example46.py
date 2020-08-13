#This is an example of the multiple inheritance


class Quadrilateral:
    """This class describes about the quadrilateral"""
    def __init__(self, a, b, c, d):
        """This is used initialize the values and perform other functions"""
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        """This is used to provide the perimeter of the quadrilateral"""
        perimeter1 = self.side1+self.side2+self.side3+self.side4
        return perimeter1

a = Quadrilateral(1,2,3,4)
print("quadrilateral perimeter",a.perimeter())

class Rectangle(Quadrilateral):
    """This class extends the Quadrilateral"""
    def __init__(self, a, b):
        super().__init__(a,b,a,b)

    def area(self):
        area = self.side1*self.side2
        return area

r = Rectangle(2,3)
print("rectangle perimeter",r.perimeter())
print("rectangle area",r.area())

class Square(Rectangle):
    """This class extends the Square"""
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        return pow(self.side1,2)

s =  Square(5)
print("square perimeter",s.perimeter())
print("square area", s.area())
