"""
This is an example of the class which elaborates on the "is"
"""

class Fraction:
    """This class describes the mathematical fraction"""
    def __init__(self, top, bottom):
        """This is used to initialize the numerator and denominator with top and bottom"""
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        """This represents the fraction in the string format"""
        return str(self.numerator)+"/"+str(self.denominator)

myfraction = Fraction(3,4)
yourfraction = Fraction(3,4)
ourfraction = myfraction

print(myfraction is ourfraction)
print(myfraction is yourfraction)