"""
Context manager is a class with __enter__ and __exit__ method
"""

class ExampleContextManager():
    """This is an example of the context manager"""
    def __init__(self):
        print('Init method is called')

    def __enter__(self):
        print('enter method is called')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit method is called')

with ExampleContextManager() as ECM:
    print('Working with the context manager')