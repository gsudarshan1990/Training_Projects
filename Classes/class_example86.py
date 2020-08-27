#This is another example of the class with property


class ReadOnly:
    def __init__(self):
        self._constant = 24

    @property
    def constant(self):
        return self._constant

r = ReadOnly()
print('The constant value is ',r.constant)
try:
    r.constant=27
except AttributeError as a:
    print(a)

class ReadWrite(ReadOnly):

    @property
    def constant(self):
        return self._constant

    @constant.setter
    def constant(self, value):
        if type(value) == int:
            self._constant = value
        else:
            raise TypeError('Integers are only allowed')

r = ReadWrite()
r.constant=29
print(r.constant)
try:
    r.constant='true'
except TypeError as t:
    print(t)
