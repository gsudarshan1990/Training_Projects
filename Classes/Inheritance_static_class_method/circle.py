from Classes.Inheritance_static_class_method.shape import Shape

import math
class Circle(Shape):
    """This class describes about the circle which forms is a relationship with shape"""
    all_circles =[]
    def __init__(self,  x =0, y=0, radius=1):
        super().__init__(x,y)
        self.radius = radius
        self.__class__.all_circles.append(self)

    @classmethod
    def total_area(cls):
        """This function describes about the area of all the triangles"""
        cummulative_area =0
        for c in cls.all_circles:
            cummulative_area+=cls.area(c.radius)
        return cummulative_area

    @classmethod
    def total_perimeter(cls):
        """This provides the total perimeter of all the circles"""
        cummulative_perimeter = 0
        for c in cls.all_circles:
            cummulative_perimeter+=c.perimeter(c.radius)
        return cummulative_perimeter

    @staticmethod
    def perimeter(radius):
        return 2*math.pi*radius

    @staticmethod
    def area(radius):
        return math.pi*(radius**2)

    def __repr__(self):
        """This represents the Circle class in the string form"""
        return "Circle("+str(self.radius)+")"

c1 =Circle()
print(c1.radius,c1.x,c1.y)
c2  = Circle(1, 1, 2)
print(c2.radius,c2.x, c2.y)
c2.move(2,2)
print(c2.radius,c2.x,c2.y)
print(c1.total_area())
print(c2.total_area())
print(c1.total_perimeter())
print(c2.total_perimeter())