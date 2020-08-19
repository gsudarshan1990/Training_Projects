"""
This describes the class
"""

import datetime

class Person:
    """This is used to describe about the Person"""
    def __init__(self, name):
        """This is used to initialize the values"""
        self.name = name
        self.birthday = None
        self.lastname = self.name.split(' ')[-1]

    def getLastName(self):
        """This is used to return the last name"""
        return self.lastname

    def setBirthday(self, year, month, day):
        """This is used to set the birthday"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """This is used to obtain the age"""
        if self.birthday == None:
            raise ValueError
        else:
            return (datetime.date.today() - self.birthday)*day

    def __lt__(self, other):
        """This is used to return the which name is shortest"""
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        """This is used to return the name"""
        return self.name


if __name__ == '__main__':
    p1  = Person('Mark Zukerberg')
    p1.setBirthday(1984,5,14)
    p2 = Person('Drew Houston')
    p2.setBirthday(1983,4,3 )
    p3 = Person('Bill Gates')
    p3.setBirthday(1955,10,28)
    p4 = Person('Andrew Gates')
    p5 = Person('Steve Woznaik')
    personlist = [p1, p2, p3, p4, p5]
    for element in personlist:
        print(element)
    personlist.sort()
    print()
    for element in personlist:
        print(element)