"""
This example checks whether two mathematical fractions are same rational
"""

def samerational(fraction1, fraction2):
    return fraction1.getNumerator()*fraction2.getDenominator() == fraction2.getNumerator()*fraction1.getDenominator()

class Fraction:
    """This class represents the mathematical fraction"""
    def __init__(self, top, bottom):
        """This initializes the mathematical numerator and denominator"""
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        """This represents the fraction in the string format"""
        return str(self.numerator)+"/"+str(self.denominator)

    def getNumerator(self):
        """This returns the numerator"""
        return self.numerator

    def getDenominator(self):
        """This returns the denominator"""
        return self.denominator

myfraction = Fraction(3,4)
yourfraction = Fraction(3,4)
print(myfraction is yourfraction)
print(samerational(myfraction,yourfraction))
otherfraction = Fraction(15,20)
print(samerational(myfraction,otherfraction))