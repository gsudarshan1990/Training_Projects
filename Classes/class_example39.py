#This is an example of the class with default and non default argument constructors


class Car:
    """This is used to describe the car"""
    def __init__(self, make, model ="550i"):
        """This is used to initialize the values"""
        self.make = make
        self.model = model

car1 = Car("bmw")
print(car1.make)
print(car1.model)

car2 = Car("benz")
print(car2.make)
print(car2.model)