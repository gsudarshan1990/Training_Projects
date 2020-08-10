"""
This is another example of the class
"""

class Fraction:
    """This class explains about the mathematics fractions"""
    def __init__(self, top, bottom):
        """This is used to initialize the values"""
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def getnumerator(self):
        """This provides the numerator"""
        return self.numerator

    def getdenominator(self):
        """This provides the denominator"""
        return self.denominator


fract1 = Fraction(10,7)
print(fract1)
print(fract1.getnumerator())
print(fract1.getdenominator())