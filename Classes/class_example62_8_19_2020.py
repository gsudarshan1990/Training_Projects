"""
This is an example of class with property
"""

class Temperature:
    """This class describes about the temperature"""
    def __init__(self, temperature = 0):
        """This is used to initialize the values"""
        self.temperature = temperature

    @property
    def farenheit(self):
        self.temperature = (self.temperature*1.8)+32

t1 = Temperature(10)
t1.farenheit
print(t1.temperature)