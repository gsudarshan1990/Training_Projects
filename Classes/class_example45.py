#This is another example of the class which is used for the initialization


class Dog:
    """This class is used to describe about the dog"""
    def __init__(self, name, age):
        """This is used to initialize the values and perform other function"""
        print('Instance of the dog created')
        self.name = name
        self.age = age

    def bark(self):
        print('Dogs bark')

    def doginfo(self):
        print('name is '+self.name+" age is "+str(self.age))

    def birthday(self):
        self.age+=1

    def setbuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self


d1 = Dog("jimmy",2)
print(d1.name)
print(d1.age)

print('name is '+d1.name+' age is '+str(d1.age))
print('*'*20)
print("Usage of the methods on the class")
d1.bark()
d1.doginfo()
d1.birthday()
print('new age:'+str(d1.age))
d2 = Dog("jack",3)
d1.setbuddy(d2)
print(d2.buddy.name)
print(d1.buddy.name)

