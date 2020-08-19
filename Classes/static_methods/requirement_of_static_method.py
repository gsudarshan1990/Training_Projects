"""
This python program describes about the necessity of the static method
"""

def price_to_book_value(market_price_per_book, book_value_per_share):
    market_price_per_book*book_value_per_share


class Book_Price_Calculator:
    PER_PAGE_PRICE = 8

    def __init__(self, pages, author):
        """This is used to initialize the values"""
        self.pages = pages
        self.author = author

    @property
    def standard_price(self):
        return self.pages*self.PER_PAGE_PRICE

"""Here price to book ratio can be even in included in class as well """