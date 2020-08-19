"""
This is another example for the inheritance
"""
from Classes.Inheritance.class_example59 import *

class Fixed(Mortgage):
    """This provides the fixed mortgage"""
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, '+str(round(r*100,2))+'%'

class FixedWithPts(Mortgage):
    """This provides the fixed mortgage along with some points"""
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid =[(loan)*(pts/100)]
        self.legend = 'Fixed, '+str(round(r*100,2))+'%,'+str(self.pts)+' Points'

class Tworate(Mortgage):
    """This provides the two rate mortgage along with some points"""
    def __init__(self, loan, r, months, teaserrate, teasermonth):
        Mortgage.__init__(self, loan, teaserrate, months )
        self.teaserrate = teaserrate
        self.teasermonth = teasermonth
        self.nextRate = r/12
        self.legend = str(teaserrate*100)+'%,'+str(teasermonth)+'months, then'+str(round(r*100,2))

    def makepayment(self):
        if len(self.paid) == self.teasermonth+1:
            self.rate = self.nextRate
            self.payment = findpayment(self.outstanding[-1], self.rate,self.months-self.teasermonth)
        Mortgage.makepayment(self)


def compareMortgages(amt, year, fixedrate, ptsrate, pts, varrate1, varrate2, varmonth):
    total_months = year*12
    fixed1 = Fixed(amt,fixedrate,total_months)
    fixed2 = FixedWithPts(amt,ptsrate,total_months, pts)
    tworate = Tworate(amt, varrate1,total_months,varrate2,varmonth)
    morts = [fixed1, fixed2, tworate]
    for m in range(total_months):
        for mort in morts:
            mort.makepayment()
    for m in morts:
        print(m)
        print('Total Payment'+str(int(m.getTotalPaid())))\

compareMortgages(amt= 200000, year=30, fixedrate=0.07, ptsrate=0.05, pts=3.25,varrate1=0.045, varrate2=0.095, varmonth=48 )
