"""
This is the singleton example class
"""

class Singleton:
    """
    This is the example of singleton class
    """
    __instance = None

    def __init__(self):
        if self.__instance == None:
            self.__instance = self
        else:
            raise Exception('This class create object only once')

    @staticmethod
    def getInstance():
        if not Singleton.__instance:
            Singleton()
        return Singleton()

s1 = Singleton()
s2 = s1.getInstance()
s3 = s1.getInstance()
print(s1)
print(s2)
print(s3)
