#This python program describes about initialization


class Student:

    def __init__(self):
        print('Initialization called')

s1 =Student()

s2 = Student()
s3 = Student()

"""
obtains the error
class Student2:

    def __init__():
        print('Initializaiton called')

s1 = Student2()
"""

class Student3:
    def __init__(boo):
        print('Initialization called')

s5 = Student3()