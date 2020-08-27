#This is another example of the property


class HardWay:
    '''Represents the Class'''
    def __init__(self, value = True):
        '''Initializes the values'''
        self.hardset(value)

    harddoc = 'Properties contain Getter, Setter, Deleter and Documentation'
    def hardset(self, value):
        if value:
            self.way = True
        else:
            self.way = False

    def hardget(self):
        return self.way

    def harddel(self):
        self.way = None

    hard = property(fget=hardget, fset= hardset, fdel=harddel, doc=harddoc)

not_decorated = HardWay()
not_decorated.hard = 'test'
print(not_decorated.hard)
del not_decorated.hard
print(not_decorated.hard)