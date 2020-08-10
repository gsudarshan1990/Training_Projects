"""
This is an example of the class which uses Getters and Setter Methods
"""

class BankAccount:
    """This class describes about the bank balance"""
    def __init__(self, name, balance = 0.0):
        """This is used to initialize the values"""
        self.log("Account Created")
        self.name = name
        self.balance = balance

    def getBalance(self):
        """This is used to obtain the balance"""
        self.log("Current Balance is "+str(self.balance))
        return self.balance

    def setBalance(self,balance):
        """This is used to set the balance"""
        self.log("Balance is set "+str(balance))
        self.balance = balance

    def log(self,message):
        mylog = open("log.txt","a")
        print(message,file=mylog)
        mylog.close()

ba = BankAccount("James")
ba.setBalance(20.0)
print(ba.getBalance())