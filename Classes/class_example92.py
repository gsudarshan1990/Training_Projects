#This is an example of the python with the special __mul__ example


print(int.__mul__(2,3))
print(float.__mul__(2.3,4.6))

class Savings:
    """This class about the amount on the bank"""
    def __init__(self, amount):
        """This is used to initialize the values"""
        self.__amount = amount

    def __add__(self, other):
        return self.__amount+other.__amount

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.__amount * other
        else:
            raise ValueError("Can multiply with only int and float")

s1 = Savings(1000)

s2 = Savings(2000)

print(s1+s2)

print(s1*4)