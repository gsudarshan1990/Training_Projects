#This is python program on the context manager

class ContextManager:
    def __init__(self):
        print('Init method is called')

    def __enter__(self):
        print('Enter method is called')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit method is called')

with ContextManager() as p:
    print('Usage of the context manager')

