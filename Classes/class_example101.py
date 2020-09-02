#This python page describes about the class method


class Competition:

    __raise_amount = 1.05

    def __init__(self, name , price):
        """this is used to initialize the values"""
        self.__name = name
        self.__price = price

    def raise_price(self):
        '''This is used to raise the price'''
        self.__price = self.__raise_amount * self.__price

    def print_details(self):
        '''This is used to print the details'''
        print( " {} {}".format(self.__name,self.__price))

    @classmethod
    def get_raise_amount(cls):
        return cls.__raise_amount

    @classmethod
    def set_raise_amount(cls, raiseamount):
        cls.__raise_amount = raiseamount

    @classmethod
    def from_str(cls, competition_str):
        '''This is used to obtain the create object from competion_str'''
        name, price = competition_str.split('-')
        return cls(name,price)