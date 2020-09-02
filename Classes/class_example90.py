"""
This is an example of the class addition
"""


print(str.__add__('a','b'))

class Savings:
    """This class is used for the savings"""
    def __init__(self, amount):
        """This is used to initialize the values"""
        self.__amount = amount

    def __add__(self, other):
        return self.__amount + other.__amount


s1 = Savings(1000)

s2 = Savings(2000)

print(s1+s2)