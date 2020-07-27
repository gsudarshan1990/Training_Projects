"""
This is another example of the closure which uses the variable declared on the outer function
"""

def get_hello_function(name):
    """
    This is the outer function
    :param name: arg1 and name of the person to be greeted
    :return: greet function
    """
    greeting = 'Hi there! '
    def greet_person():
        """
        This is the inner function
        :return: Nothing
        """
        print(greeting,name)
    return greet_person

hello_fn = get_hello_function('Chris')
hello_fn()