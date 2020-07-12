"""
This class explains about the factory method
"""

class Cup:
    """
    This class describes about the cup
    """
    def factory(cupcolor):
        """
        This describes about the type of cup to be returned
        :return: returns the object
        """
        if cupcolor =='red':
            return RedCup()
        elif cupcolor =='green':
            return GreenCup()

class RedCup:
    def contains(self):
        print('This cup contains the coffee')

class GreenCup:
    def contains(self):
        print('This cup contains the tea')


cup_type = Cup.factory('red')
cup_type.contains()