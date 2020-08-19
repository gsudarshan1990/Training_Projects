"""
This is another example of the class with the setter methods
"""

class Temperature:
    """This class is used to provide the temperature"""
    def __init__(self, temperature = 0):
        """This is used to initialize the values"""
        self._temperature = temperature

    @property
    def farenheit(self):
        return self._temperature

    @farenheit.setter
    def fareneheit(self, temp):
        if not isinstance(temp, int):
            print('Wrong Input')
        self._temperature = (self._temperature*1.8)+32