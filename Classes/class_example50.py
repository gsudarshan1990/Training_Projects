"""This is an example of the class which elaborates on the encapsulation"""


class Person:
    """This class describes about the person"""
    def __init__(self, name):
        """This is used to initialize the values"""
        self.name = name

    def _protected(self):
        print('This is protected method')

    def __private(self):
        print("This is a private method")

if __name__ =='__main__':
    p = Person('Jack')
    p._protected()
    #p.__private() throws the attribute errror
