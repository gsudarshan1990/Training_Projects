#This python program is about the class variable


class Competition:
    '''This is about the competition'''
    participants = []
    def __init__(self, name, price):
        '''This is used to initialize the values'''
        self.name = name
        self.price = price

debate = Competition('Debate',500)
print(debate.participants)
Competition.participants.append('Alice')
print(Competition.participants)
print(debate.participants)
debate.participants.append('John')
print(Competition.participants)
print(debate.participants)
essay = Competition('Essay',500)
print(essay.participants)
essay.participants.append('lily')
print(essay.participants)