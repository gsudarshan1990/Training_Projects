#This is another example of the class

import sys
import locale

class BaseModel:
    """This is the base model"""
    trim = 'normal'
    engine_liters = 1.5
    miles_range = 450
    tank_capacity = 45
    color = 'white'
    transmission = 'automatic'

    @classmethod
    def miles_per_liter(cls):
        return cls.miles_range/cls.tank_capacity

    @classmethod
    def miles_per_gallon(cls):
        return cls.miles_per_liter()*3.78514

    def __init__(self, price, transmission = 'automatic', color ='white'):
        """This is used to initialize the values"""
        self.price  = price
        self.transmission = transmission
        self.color = color

    def info(self):
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL,'us')
        else:
            locale.setlocale(locale.LC_ALL, 'en-us.utf8')
        print('%s car is price %s'%(self,locale.currency(self.price)))

    def __str__(self):
        return 'a %s color has %s transmission'%(self.color, self.transmission)

coop = BaseModel(25000)
coop.info()
print('%s has %s gallons'%(coop, coop.miles_per_gallon()))
print('%s has %s gallons'%(BaseModel, BaseModel.miles_per_gallon()))

class Sport_Model(BaseModel):
    """This class represents the sports car"""
    engine = 2
    miles_range = 400

coop_sports = Sport_Model(color ='red', transmission='automatic', price = 26000)
print ('%s has %4.1f miles per gallon'%(coop_sports, coop_sports.miles_per_gallon()))