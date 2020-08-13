#This is used to describe the inheritance


class Car:
    """This is used to describe about the car"""
    def __init__(self):
        print("Car instance has been created")

    def start(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")

class BMW(Car):
    """This is used to describe the BMW which forms the is a relationship with the car"""
    def __init__(self):
        Car.__init__(self)
        print('BMW instance is created')

c= Car()
c.start()
c.stop()

print('*'*20)
b = BMW()
b.start()
b.stop()