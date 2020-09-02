#This python program is about class and instance variables



class Competition:
    '''This class describes about the competition'''
    raise_amount = 1.04
    def __init__(self, name, price):
        '''This is used to initialize the values'''
        self.name = name
        self.price = price

    def raise_price(self):
        self.price = self.price* self.raise_amount

simulation = Competition('Simulation',100)
print(simulation.name)
print(simulation.price)
print(simulation.raise_amount)
simulation.raise_price()
print(simulation.price)
racing = Competition('racing',100)
print(racing.name)
print(racing.price)
print(racing.raise_amount)
racing.raise_price()
Competition.raise_amount=1.05
print(Competition.raise_amount)
print(simulation.raise_amount)
print(racing.raise_amount)
print(simulation.__dict__)
print(Competition.__dict__)

