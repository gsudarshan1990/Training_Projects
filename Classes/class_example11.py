"""
This is an example of the class which is used to encapsulate other functions
"""

class BankAccount:
    """This class is used to describe the bank account"""
    def __init__(self, name, balance = 0.0):
        """This is used to initialize the values"""
        self.log("Account Created")
        self.name = name
        self.balance = balance

    def getBalance(self):
        """This is used to provide the balance"""
        self.log("Balance is "+str(self.balance))
        return self.balance

    def deposit(self, amount):
        """This is used certain amount to the balance"""
        self.initial_balance = self.balance
        self.balance+=amount
        self.log(str(self.initial_balance)+"+"+str(amount)+":"+str(self.balance))

    def withdraw(self, amount):
        """This is used to decrease certain amount of balance"""
        self.initial_balance = self.balance
        self.balance-=amount
        self.log(str(self.initial_balance)+"-"+str(amount)+":"+str(self.balance))

    def log(self, message):
        """This is used to log the events"""
        mylog = open("log2.txt","a")
        print(message, file = mylog)
        mylog.close()

ba = BankAccount("Johnathan")
ba.deposit(20.0)
print(ba.getBalance())
ba.withdraw(5.0)
print(ba.getBalance())
ba.deposit(125.0)
print(ba.getBalance())
ba.withdraw(75.0)
print(ba.getBalance())