
#Classes can also have references to other instances of
#themselves. Consider this Person class with name and ange, for example,
#that allows for an instance of a father and mother
#to be given in the constructor.
#
#Create 3 instances of this class. The first should have
#the name "Mr. Burdell" with an age of 53. The second
#instance should have a name of "Mrs. Burdell" with an age
#of 53 as well. Finally, make an instance with the name of
#"George P. Burdell" with an age of 25. This final instance
#should also have the father attribute set to the instance
#of Mr. Burdell, and the mother attribute set to the
#instance of Mrs. Burdell. Finally, store the instance of
#George P. Burdell in a variable called george_p.

class Person:
    """This class describes a normal Person"""
    def __init__(self, name, age, father=None, mother=None):
        """This is used to initialize the values and sets the name and age along with father and mother if provided"""
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

p1 = Person("Mr. Burdell",53)
p2 = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, p1, p2)
print(george_p.name)
print(george_p.father.name)
print(george_p.mother.name)