"""
This is another example of the class
"""

class BaseModel:
    """This class represents the base model of the class"""
    trim ='normal'
    engine_liters = 1.5

    def engine_sound(self):
        return 'putt, putt'

    def horn_sound(self):
        return 'beep, beep'

    def __str__(self):
        return 'Base Model'

coop = BaseModel()
print('%s has %s model '%(coop, coop.trim))
print('%s has %s engine liters'%(coop, coop.engine_liters))
print('%s has %s engine sound'%(coop, coop.engine_sound()))
print('%s has %s horn sound'%(coop, coop.horn_sound()))