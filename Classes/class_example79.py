#This is an example of the class with the inheritance

class BaseModel:
    '''This represents the base model of the car'''
    trim = 'normal'
    engine_liters = 1.5

    def engine_sound(self):
        return 'putt, putt'

    def horn_sound(self):
        return 'beep, beep'

    def __str__(self):
        return 'BaseModel'

coop = BaseModel()
print('%s has %s trim'%(coop, coop.trim))
print('%s has %s engine_liters'%(coop, coop.engine_liters))
print('%s has %s engine_sound'%(coop, coop.engine_sound()))
print('%s has %s horn sound '%(coop, coop.horn_sound()))

class SportsModel(BaseModel):
    '''Represents the Sports Model'''
    engine_liters = 2.0

    def engine_sound(self):
        return 'VROOM, VROOM'

    def horn_sound(self):
        return 'BEEP, BEEP'

    def __str__(self):
        return 'sports model'

sports = SportsModel()
print('%s has %s trim'%(sports, sports.trim))
print('%s has %s engine_liters'%(sports, sports.engine_liters))
print('%s has %s engine sound'%(sports, sports.engine_sound()))
print('%s has %s horn sound'%(sports, sports.horn_sound()))

class Luxury_Model(BaseModel):
    '''Represents the Luxury Model car'''
    trim ='luxury'

    def engine_sound(self):
        return 'vroom, vroom'

    def horn_sound(self):
        return 'honk, honk'

    def __str__(self):
        return 'Luxury Model'

luxury = Luxury_Model()
print('%s has %s trim'%(luxury, luxury.trim))
print('%s has %s engine_liters'%(luxury, luxury.engine_liters))
print('%s has %s engine sound'%(luxury, luxury.engine_sound()))
print('%s has %s horn sound'%(luxury, luxury.horn_sound()))

class Luxury_Sports_Model(Luxury_Model, SportsModel):
    def __str__(self):
        return 'Luxury Sports Model'

lsm = Luxury_Sports_Model()
print('%s has %s trim'%(lsm, lsm.trim))
print('%s has %s engine_liters'%(lsm, lsm.engine_liters))
print('%s has %s engine_sound'%(lsm, lsm.engine_sound()))
print('%s has %s horn sound'%(lsm, lsm.horn_sound()))

class Sports_Luxury_Model(SportsModel, Luxury_Model):
    def __str__(self):
        return 'Sports Luxury Model'

slm = Sports_Luxury_Model()
print('%s has %s trim'%(slm, slm.trim))
print('%s has %s engine_liters'%(slm, slm.engine_liters))
print('%s has %s engine sound '%(slm, slm.engine_sound()))
print('%s has %s horn sound'%(slm, slm.horn_sound()))
