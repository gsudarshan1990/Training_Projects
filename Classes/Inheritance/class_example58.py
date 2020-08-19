from Classes.Inheritance.class_example57 import Person

class MITPerson(Person):
    """This class describes about the person from MIT"""
    nextIdnum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.Idnum = MITPerson.nextIdnum
        MITPerson.nextIdnum+=1

    def getIdNum(self):
        """This returns the MIT ID num"""
        return self.Idnum

    def __lt__(self, other):
        """Return whose Id is first"""
        return self.Idnum < other.Idnum

    def speak(self, utterance):
        return (self.getLastName()+" says:"+utterance)

p1 = MITPerson('Eric')
p2 = MITPerson('John Gutag')
p3 = MITPerson('John Smith')
p4 = Person('John')

if __name__ == '__main__':
    p1 = MITPerson('Mark Zukerberg')
    p1.setBirthday(1984,5,14)
    p2 = MITPerson('Drew Houston')
    p2.setBirthday(1983,4,3)
    p3 = Person('Travis Kalanik')
    p4 = Person('Steve Woznaik')
    personlist = [p1,p2,p3,p4]
    for person in personlist:
        print(person)
    personlist.sort()
    print()
    for person in personlist:
        print(person)
