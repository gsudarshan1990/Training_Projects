#This is another example of the property


class Student:
    '''This class describes about the marks of the student'''
    def __init__(self, score):
        self._score =score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, newscore):
        if newscore>100 or newscore<0:
            raise ValueError('Invalid Score')
        self._score = newscore

    @score.deleter
    def score(self):
        self._score = None

student = Student(99)
print(student.score)
try:
    student.score=101
except ValueError as e:
    print(e)

try:
    student.score=98
except ValueError as e:
    print(e)

print(student.score)
del student.score
print(student.score)

