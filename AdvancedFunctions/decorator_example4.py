"""
This is an example of the chained decorator
"""

def asterik_highlight(func):
    """
    This is surround function with asterik
    :param func: arg1 and is function object
    :return: function object
    """
    def inner_func():
        print('*'*50)
        func()
        print('*'*50)
    return inner_func

def plus_highlight(func):
    """
    This is surround the function with the plus sign
    :param func: arg1 and is function object
    :return: function object
    """
    def inner_func():
        print('+'*50)
        func()
        print('+'*50)
    return inner_func

@plus_highlight
@asterik_highlight
def print_message():
    print('Yahoooooo!, Decorators are cool')

print_message()

print("="*50)

print()
print()

@asterik_highlight
@plus_highlight
def print_message():
    print('Yahoooooooo! Decorators are cool')

print_message()