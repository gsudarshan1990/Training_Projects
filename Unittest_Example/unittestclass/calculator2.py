"""
This creates the class which raises exceptions and which needs to be tested
"""

class SecondCalculator:
    """This is used to calculate the addition of two numbers"""
    def add(self,x,y):
        """This adds two numbers"""
        if type(x) == int and type(y) == int:
            return x+y
        else:
            raise TypeError("{}  and {}  is not in appropriate format".format(x,y))

if __name__ == '__main__':
    scalc = SecondCalculator()
    result =scalc.add(2,3)
    print(result)
    