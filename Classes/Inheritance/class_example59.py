"""
This class describes about the mortgage
"""

def findpayment(loan, r, m):
    """This return the payment"""
    return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage:
    """This class defines about the mortgage"""
    def __init__(self, loan, annRate, months ):
        """This is used to initialize the values"""
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findpayment(self.loan,self.rate,self.months)
        self.legend = None

    def makepayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1]-reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend
