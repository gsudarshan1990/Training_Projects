#This is an example of the class


class Car:
    """This is used to describe the class"""
    wheels = 4
    def __init__(self, make, model):
        """This is used to initialize the values"""
        self.make = make
        self.model = model

    def info(self):
        """This is used to describe about the car"""
        print('Make of the car is '+self.make)
        print('Model of the car is '+self.model)

car1 = Car("bmw","550i")
car2 = Car("Benz","E550")

print(car1.model)
print(car1.model)
car1.info()
print(car2.make)
print(car2.model)
car2.info()
print(Car.wheels)