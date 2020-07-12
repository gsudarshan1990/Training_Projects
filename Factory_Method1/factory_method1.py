"""
This is the example of the factory method
"""

class Car:
    """
    This is the factory class
    """
    @staticmethod
    def factory(type):
        """
        Descrbies about type of the Car
        :return: object
        """
        if type == 'RaceCar':
            return RaceCar()
        elif type == 'MotorCar':
            return MotorCar()


class RaceCar:
    def drive(self):
        print('This is Race car')

class MotorCar:
    def drive(self):
        print('This is the Motor Car')

car1 = Car.factory('RaceCar')
car1.drive()