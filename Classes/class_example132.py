#This is another python example


class Father:

    def height(self):
        print('I have inherited height from my father')


class Mother:
    def intelligence(self):
        print('I have inherited intelligence from my mother')

class Child(Father, Mother):
    def experience(self):
        print('I have my experience of my own')

child = Child()
child.height()