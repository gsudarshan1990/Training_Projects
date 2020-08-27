"""
This is an example of the class
"""

class Grader:
    '''This class represents the score of a student'''
    def __init__(self, score = 0):
        '''This is used to initialize the values'''
        self.score = score

math1 = Grader(90)
print('%d is the score'%(math1.score))
math1.score=101
print('%d is the score'%(math1.score))
#Here Score cannot be greater than 100 and this is sorted in class_example81
