"""
This is another example of the closure which takes the parameter and gets utilized in the inner function
"""

def use_hello_function(name):
    """
    This is the example of the closure function
    :param name: arg1 and name of the person to be greeted
    :return: a function object
    """
    def hello():
        print('Greet', name)

    hello()
    return hello

greet_hello_fn = use_hello_function('Alex')
greet_hello_fn()