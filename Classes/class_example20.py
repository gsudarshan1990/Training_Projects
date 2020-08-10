"""
This is another example of the class
"""

class Fraction:
    """This class is used to describe about the mathematical fractions"""
    def __init__(self, top, bottom):
        """This is used to initialize the values"""
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        """This is used to describe the fraction"""
        return str(self.numerator)+"/"+str(self.denominator)

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __add__(self, other):
        """This is used to add two fractions"""
        self.numerator1 = self.numerator*other.denominator+self.denominator*other.numerator
        self.denominator1 = self.denominator*other.denominator
        return Fraction(self.numerator1,self.denominator1)

    def __sub__(self, other):
        """This is used to subtract two fractions"""
        self.numerator1 = self.numerator * other.denominator - self.denominator * other.numerator
        self.denominator1 = self.denominator * other.denominator
        return Fraction(self.numerator1, self.denominator1)

    def convert(self):
        """This is used to convert the values"""
        return self.getNumerator()/self.getDenominator()

f1 = Fraction(4,7)
f2 = Fraction(10,3)
print(f1+f2)
print(f1-f2)
print(f1.convert())
print(f2.convert())
print((f1+f2).convert())