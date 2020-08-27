#This is another example of class


import locale
import sys

class Base_Model:
    """This class describes about the car model"""
    trim = 'normal'
    engine_liters = 1.5

    def __init__(self, price, transmission = 'manual', color ='white'):
        """This is used to initialize the values"""
        self.price = price
        self.transmission = transmission
        self.color = color

    def info(self):
        """This is used to initialize the values"""
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL, 'US')
        else:
            locale.setlocale(locale.LC_ALL,'en-US.utf-8')
        print('The price of %s is %s'%(self, locale.currency(self.price)))

    def __str__(self):
        return 'a %s color with %s method '%(self.color,self.transmission)

coop = Base_Model(25000)
coop.info()

coop_blue = Base_Model(25500, color='blue')
coop_blue.info()

coop_manual_red = Base_Model(26000,transmission='manual',color='red')
coop_manual_red.info()

coop_manual_green = Base_Model(price = 26500, transmission='manual',color ='green' )
coop_manual_green.info()