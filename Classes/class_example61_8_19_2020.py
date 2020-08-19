"""
This is a python program which elaborates on the class

"""

class Door:
    """This class describes about the door"""
    height = 7
    color = 'brown'

    def status(self):
        return 'Door is locked'

    def doortype(self):
        return 'Door is made of the wood'

    def __str__(self):
        return 'Door'

d = Door()
print( '%s is of %d cm height'%(d, d.height))
print('The color of %s is %s '%(d, d.color))
print('The status of %s is: %s status'%(d, d.status()))
print('The %s is made up of: %s'%(d, d.doortype()))