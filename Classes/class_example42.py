"""This class is used to describe the polymorphism"""

class Car:
    """This is used to describe the car"""
    def __init__(self):
        """This is used to initialize and perform other actions while initialization"""
        print('Car Instance is created')

    def drive(self):
        """This describes when car started to run"""
        print('Car is started and running')

    def stop(self):
        """This describes when car is stopped"""
        print('Car is stopped ')


class BMW(Car):
    """This is used to describe the BMW which forms a is a relationship with the Car"""
    def __init__(self):
        """This is used to initialize and perform other operations while creating the instances"""
        Car.__init__(self)
        print('BMW instance is created')

    def drive(self):
        """This is used extended the above function through the method overriding process"""
        super().drive()
        print('BMW is started running')

    def headsup_display(self):
        """This is used to display the light"""
        print('BMW contains the headsup display')

c = Car()
c.drive()
c.stop()
print('*'*20)
b = BMW()
b.drive()
b.headsup_display()
b.stop()