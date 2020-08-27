#This is an example of the class with static methods

import sys
import locale

class BaseModel:
    '''Represents the base model of the car'''
    trim = 'normal'
    engine_liters = 1.5
    miles_per_range = 450
    tank_capacity = 45
    color = 'white'
    transmission = 'automatic'

    @staticmethod
    def miles_per_liter(miles_range, tank_capacity):
        return miles_range/tank_capacity

    def miles_per_gallon(miles_range,tank_capacity):
        return BaseModel.miles_per_liter(miles_range,tank_capacity)*3.78514
    miles_per_gallon = staticmethod(miles_per_gallon)

    def __init__(self, price, transmission = 'automatic',  color ='white'):
        '''This is used to initialize the values'''
        self.price = price
        self.transmission = transmission
        self.color = color

    def info(self):
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL, 'us')
        else:
            locale.setlocale(locale.LC_ALL, 'en-us.utf8')
        print('%s with the price %s'%(self,locale.currency(self.price)))

    def __str__(self):
        return '%s has %s transmission'%(self.color, self.transmission)

coop = BaseModel(25000)
coop.info()
print('%s has %4.1f gallons'%(coop, coop.miles_per_gallon(coop.miles_per_range,coop.tank_capacity)))
print('%s has %4.1f gallons '%(BaseModel, BaseModel.miles_per_gallon(BaseModel.miles_per_range, BaseModel.tank_capacity)))

class SportsModel(BaseModel):
    '''Represents the Sports Model'''
    engine_liters = 2
    miles_per_range = 400

sports = SportsModel(27000)
sports.info()
print('%s has %4.1f gallons '%(sports, sports.miles_per_gallon(sports.miles_per_range,sports.tank_capacity)))

