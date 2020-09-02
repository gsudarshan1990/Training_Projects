#This is an example of __repr__


class SportsCompetion:
    """This class represents differente sports competition and values"""
    def __init__(self, name, price):
        """This is used to initialize the values"""
        self.__name = name
        self.__price = price

    def __repr__(self):
        return "({}, {})".format({self.__name},{self.__price})

archery = SportsCompetion("archery", 8000)
print(archery)
print(repr(archery))