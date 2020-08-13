"""
This is another example  of the class
"""

def hi(obj):
    print('Hi name is '+obj.name)

class Robot:
    say_hi = hi

x = Robot()
x.name = 'Maxwell'
Robot.say_hi(x)