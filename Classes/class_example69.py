#This is another example of the class with Composition and Property

class Account:
    """This class describes about the student account"""
    def __init__(self, student_id):
        """This is used to initialize the values"""
        self.student_id = student_id
        self.balance = 400

    @property
    def balance(self):
        return self.balance

    balance.setter
    def balance(self, amount):
        self.balance+=amount

class Student:
    """This class describes about the student"""
    def __init__(self, firstname, lastname, student_id):
        """This is used to initialize the values"""
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.account = Account(self.student_id)

    def check_amount_balance(self):
        return self.account.balance

    def load_balance(self, amount):
        self.account.balance+=amount

student = Student('rahul','bose','A5')
print(student.check_amount_balance())