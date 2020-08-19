"""
This explains the necessity of the static method in python program
"""

class BOOK_PER_PRICE_CALCULATOR:
    PAGE_PER_PRICE = 8

    def __init__(self, pages, author):
        """This is used to initialize the values"""
        self.pages = pages
        self.author = author

    @property
    def standard_price(self):
        return self.pages*self.PAGE_PER_PRICE

    @staticmethod
    def BOOK_PRICE_MARKET_VALUE(market_price_per_book,book_value_per_share):
        return market_price_per_book/book_value_per_share