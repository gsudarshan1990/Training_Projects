#This is an example of the composition


class Account:
    """This class describes about the account of a student"""
    def __init__(self, student_id):
        """This is used to initialize the values and also sets the balance"""
        self.student_id = student_id
        self.balance = 400

    def get_balance(self):
        """This is used to return the balance"""
        return self.balance

    def set_balance(self, amount):
        """This is used to set the balance"""
        self.balance+=amount

class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname, student_id):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.account = Account(self.student_id)

    def check_account_balance(self):
        self.account.get_balance()

    def add_amount(self, amount):
        self.account.set_balance(amount)