#This python pages describes about length function

print(len('test'))

print(str.__len__('hello'))

class Participants:
    """This class describes about the Participants"""
    def __init__(self):
        """This is used to initialize the values"""
        self.__participants = []

    def add_participants(self, name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)

p = Participants()

p.add_participants('james')
p.add_participants('johnathon')
print(len(p))
