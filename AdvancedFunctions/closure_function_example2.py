"""
This is another example of the closure function
"""

def get_hello_function():
    """
    This is the outer function
    :return: a function object
    """
    def hello():
        """
        This is the inner function
        :return: Nothing
        """
        print('Hello Cathy')

    return hello

hello_fn = get_hello_function()
print(hello_fn)
hello_fn()