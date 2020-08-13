"""
This is an example of the class
"""

class Dog:
    """This class describes about the dog"""
    species = "cannis familiaris"

    def __init__(self, name, age, breed):
        """This is used to initialize the values along with performing other actions"""
        self.name = name
        self.age = age
        self.breed = breed

miles = Dog("Miles",9,"Jack Russell Terrier")
buddy = Dog("buddy",5,"Dachshund")
jack = Dog("Jack",3,"Bull Dog")
jim = Dog("Jim", 6, "Bull Dog")