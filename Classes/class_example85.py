#This is another example of the class

class Grades:
    '''This describes about the class'''
    def __init__(self, score = 0):
        '''This is used to initialize the values'''
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value>100 or value<0:
            raise ValueError('Invalid Score')
        self._score = value

g = Grades(90)
print(f'the score is {g._score}')
try:
    g.score =101
except ValueError as e:
    print(e)

class Grader(Grades):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value>200 or value<0:
            raise ValueError
        self._score=value

grader=Grader(99)
print(grader.score)
try:
    grader.score=199
except ValueError as e:
    print(e)
print(grader.score)