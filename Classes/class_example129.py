#This is another python program

class Competition:
    '''This class describes about the various sports competition'''
    __raise_amount = 1.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def raise_price(self):
        self.price = self.price*Competition.__raise_amount

print(help(Competition))
print(Competition.__dict__)

class Sprint(Competition):
    pass

print(Sprint.__dict__)

print(help(Sprint))

sprint = Sprint('100m',700)

sprint.raise_price()

print(sprint.get_price())

chess = Competition('chess',1000)

chess.raise_price()
print(chess.get_price())
