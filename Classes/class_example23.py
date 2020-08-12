"""
This is an example of the class which describes the class hierarchies
"""

class Animal:
    """This is used to describe the animal"""
    def __init__(self, age):
        """This is used to initialize the values"""
        self.age = age
        self.name = None

    def getname(self):
        """This returns the name of the animal"""
        return self.name

    def getage(self):
        """This returns the age of the animal"""
        return self.age

    def setage(self, age):
        """This is used to set the age"""
        self.age = age

    def setname(self,newname ):
        """This is used to set the name"""
        self.name = newname

    def __str__(self):
        """This is used to represents the animal"""
        return "animal name:"+str(self.name)+" age:"+str(self.age)

class Cat(Animal):
    """This class represents a Cat which follows is a relationship with Animal"""
    def speak(self):
        """This function defines how cat speaks"""
        print("meow")

    def __str__(self):
        """This is used to represent the cat"""
        return "Cat name:"+str(self.name)+" age:"+str(self.age)

class Rabbit(Animal):
    """This class represents the Rabbit which follows is a relationship with Animal"""
    def speak(self):
        """This function defines how a rabbit speaks"""
        print("meep")

    def __str__(self):
        """This is used to represent the rabbit"""
        return "Rabbit name:"+str(self.name)+" age:"+str(self.age)

class Person(Animal):
    """This class represents the Person which forms the is a relationship with Animal"""
    def __init__(self, name, age):
        """This is used to initialize the values"""
        Animal.__init__(self,age)
        self.setname(name)
        self.friends=[]

    def getfriends(self):
        """This is used to return the total number of friends"""
        return self.friends

    def add_friend(self, friendname):
        """This is used to add the new friend"""
        if friendname not in self.friends:
            self.friends.append(friendname)

    def speak(self):
        """This represents how a student speak"""
        print("hello")

    def age_difference(self, other):
        """This is used to find the age difference between the two persons"""
        diff = self.age - other.age
        if diff>0:
            print(self.name+" is elder than "+other.name+"for years "+str(diff))
        else:
            print(self.name + " is elder than " + other.name + "for years " + str(abs(diff)))

    def __str__(self):
        """This is used to represent the person on the string format"""
        return "Person name:"+str(self.name)+" age:"+str(self.age)

import random
class Student(Person):
    """This class represents the Student which forms the is a relationship with Person"""
    def __init__(self, name, age, major = None):
        """This is used to initialize the values"""
        Person.__init__(self, age, name)
        self.major = major

    def changemajor(self, newmajor):
        """This is used to change the major"""
        self.major = newmajor

    def speak(self):
        r = random.random()
        if r >0.25:
            print("Student is doing the homework")
        elif 0.25<r<0.50:
            print('Student is eating')
        elif 0.50<r<0.75:
            print('Student is sleeping')
        elif 0.75<r<1.0:
            print('Student is awake')

    def __str__(self):
        """This is used to represent the string"""
        return "student name:"+str(self.name)+" age:"+str(self.age)+" major:"+str(self.major)


jelly = Cat(1)
jelly.setname('Jelly')
tiger = Cat(1)
tiger.setname('Tiger')
bean = Cat(0)
bean.setname('Bean')
print(jelly)
jelly.speak()
blob = Animal(1)
peter = Rabbit(3)
peter.speak()
eric = Person('Eric', 45)
eric.speak()
john = Person('John', 55)
eric.age_difference(john)
fred = Student('Fred', 18, 'Course VI')


