#This is an example of the class with inheritance


class Dog:
    """This class is used to describe about the dog"""
    species = "cannis familiaris"
    def __init__(self, name, age):
        """This is used to initialize the values along with the other actions"""
        self.name = name
        self.age = age

    def __str__(self):
        """This represents the in the string format"""
        return f"{self.name} age and age is {self.age}"

    def speak(self, sound):
        """This dog speaks the following"""
        return f"{self.name} speaks sound"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class BullDog(Dog):
    pass

miles = JackRussellTerrier("Miles",4)
buddy = Dachshund("buddy",6)
jack = BullDog("jack",9)
jim = BullDog("jim",7)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak('woof'))