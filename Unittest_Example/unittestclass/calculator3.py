"""
This page is used to define the calculator class
"""

class Calculator:
    """This class implements two different methods of additions"""
    def add1(self, x, y):
        """This performs the normal addition"""
        return x+y

    def add2(self, x, y):
        """This performs the addition after type checking"""
        number_types = (int, float, complex)
        if isinstance(x,number_types) and isinstance(y,number_types):
            return x+y
        else:
            raise ValueError


