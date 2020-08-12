"""
This is another example of the class which uses the inheritance
"""

class Animal:
    """This class describes the animal"""
    def __init__(self, age):
        """This is used to initialize the value"""
        self.age = age
        self.name = None

    def get_name(self):
        """This is used to return the name"""
        return self.name

    def get_age(self):
        """This is used to return the age"""
        return self.age

    def set_age(self, age):
        """This is used to set the age"""
        self.age = age

    def set_name(self, newname):
        """This is used to set the name"""
        self.name = newname

    def __str__(self):
        """This is used to represent the Animal class in string format"""
        return "Animal name:"+str(self.name)+" age:"+str(self.age)

class Cat(Animal):
    """This class represents the Cat class and forms the is a relantionship with Animal"""
    def speak(self):
        """This functions defines how a cat speaks"""
        print("meow!")

    def __str__(self):
        """This represents the cat in the string format"""
        return "Cat name:"+str(self.name)+" age:"+str(self.age)

class Rabbit(Animal):
    """This represents the Rabbit class and forms a is a relationship with the Animal"""
    tag = 0
    def __init__(self, age, parent1 = None, parent2= None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag+=1

    def get_rid(self):
        """Returns the rid"""
        return str(self.rid).zfill(3)

    def get_parent1(self):
        """This returns the parent1"""
        return self.parent1

    def get_parent2(self):
        """This returns the parent2"""
        return self.parent2

    def __add__(self, other):
        """This adds two Rabbits"""
        return Rabbit(0, self, other)

    def __eq__(self, other):
        """This checks whether two parents are equal"""
        parent_one = (self.parent1.rid == other.parent1.rid) and (self.parent2.rid == other.parent2.rid)
        parent_two = (self.parent1.rid == other.parent2.rid) and (self.parent2.rid) == other.parent1.rid
        return parent_one or parent_two

    def __str__(self):
        """This represents the Rabbit in the string format"""
        return "Rabbit name:"+str(self.name)+" age:"+str(self.age)+" parent1:"+str(self.parent1)+" parent2:"+str(self.parent2)

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
mopsy = peter + hopsy
print(mopsy == cotton)