#This is another python program


class Competition:
    '''This class describes about the various python programs'''
    __raise_amount = 1.1
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def raise_price(self):
        self.__price = self.get_price()*Competition.__raise_amount

class Cycling(Competition):
    '''This class forms is a relationship with the Competition'''
    def __init__(self, name, price, country):
        Competition.__init__(self, name, price)
        self.__country = country

    def get_country(self):
        return self.__country

print(Cycling.__dict__)
print(Competition.__dict__)

print(help(Cycling))

print(help(Competition))

cycling =Cycling('cycling',1000, 'India')
print(cycling.get_country())
print(cycling.get_price())
print(cycling.get_name())
print(issubclass(Cycling,Competition))
print('-'*20)
print(isinstance(cycling,Competition))
print('-'*10)
class Shooting():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

print(issubclass(Shooting,Competition))

class Shooting(Competition):
    def __init__(self, name, price):
        Competition.__init__(self, name, price)

print(issubclass(Shooting,Competition))