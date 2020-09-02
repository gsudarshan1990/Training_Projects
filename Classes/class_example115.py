#This python program is about the class variable


class Competition:
    raise_amount = 1.04

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def raise_price(self):
        self.price=self.price*Competition.raise_amount


debate = Competition('debate',500)
print(debate.raise_amount)
print(Competition.raise_amount)

debate.raise_price()
print(debate.price)

essay = Competition('Essay',800)
print(essay.price)

essay.raise_price()
print(essay.price)