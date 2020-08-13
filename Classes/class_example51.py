"""
This is another example of the class

"""

class Door:
    """This class is used to describe the door"""
    def __init__(self, height, color, locked):
        """This is used to initialize the values"""
        self.height = height
        self.color = color
        self.is_locked = locked

    def open(self):
        print('Door is open')

    def close(self):
        print('Door is closed')

    def toogle_door(self):
        print('Door is toggled')

d1 = Door(85,'orange',True)
d2 = Door(78,'blue',False)