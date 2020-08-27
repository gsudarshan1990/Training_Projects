#This is an example of the property


class Grader:
    '''This represents the score of the student'''
    def __init__(self, score = 0):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value > 100 or value <0:
            raise  ValueError("Invalid Score")
        self._score = value


math1 = Grader(90)
print('%d is the score'%(math1.score))

try:
    math1.score =101
except ValueError as e:
    print(e)
