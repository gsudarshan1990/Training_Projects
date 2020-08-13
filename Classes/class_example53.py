"""
This is another example of the class
"""

class Robot:
    pass

x = Robot()
y = Robot()
x.name = 'Marvin'
x.build_yer = 1979

y.name = 'He-man'
y.build_year = 1993

print(x.name)
print(y.build_year)

print(x.__dict__)
print(y.__dict__)