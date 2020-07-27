"""
This is an example of the closure function which deletes the outer function
"""

def greet_function(name):
    """
    This is the outer function
    :param name: arg1 and the name of the person to be greeted
    :return: function object
    """
    def hello():
        print('Hello', name)

    return hello

hello_fn = greet_function('Johnson')
hello_fn()
del greet_function
#greet_function('Jack')
hello_fn()