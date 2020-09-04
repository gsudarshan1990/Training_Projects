#This is python program on Multiple Inheritance


class GrandParent:
    def height(self):
        print('I have inherited height from Grand Parent')

class Parent(GrandParent):
    def intelligence(self):
        print('I have inherited intelligence from Parent')

class Child(Parent):
    def experience(self):
        print('I have my experience of my own')

c = Child()
c.height()
c.experience()
c.intelligence()