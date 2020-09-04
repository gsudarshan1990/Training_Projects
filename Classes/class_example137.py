#This is another python program


class BankAccount:
    '''This class describes about the bank account'''
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, value):
        self.__balance+= value

        print('Deposit amount',value)
        print('New Balance', self.__balance)

    def withdrawal(self, value):
        self.__balance-=value
        print('Value amount', value)
        print('New Balance', self.__balance)

class CurrentAccount(BankAccount):
    '''This class describes about the current account'''
    def __init__(self, balance):
        super().__init__(balance)

    def withdrawal(self, value):
        if value>1000:
            print('Contact the manager')
        else:
            super().withdrawal(value)

class SavingsAccount(BankAccount):
    '''This class describes about the saving account'''
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, value):
        value+=0.05*value
        super().deposit(value)

currentaccount = CurrentAccount(1500)

currentaccount.withdrawal(100)
currentaccount.withdrawal(1200)

savingsaccount = SavingsAccount(1500)
savingsaccount.deposit(120)
