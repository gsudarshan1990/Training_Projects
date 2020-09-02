#This python is another example of using len and inbuilt iteration


class Participants:
    """This class describes about the participants"""
    def __init__(self):
        self.__participants =[]
        self.index =0

    def add_participants(self, name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)

    def __iter__(self):
        self.index =0
        return self

    def __next__(self):
        if self.index == len(self.__participants):
            raise StopIteration
        p = self.__participants[self.index]
        self.index+=1
        return p

p1 = Participants()

p1.add_participants('James')
p1.add_participants('emily')

print(len(p1))

for part in p1:
    print(part)