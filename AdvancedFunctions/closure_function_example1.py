"""
A function within another function is an example of the closure function
"""

def use_hello_func():
    """
    This is the outer function
    :return: Nothing
    """
    def hello():
        """
        This is the inner function
        :return: Nothing
        """
        print('Greet Cathy!')
    hello()

use_hello_func()