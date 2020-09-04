#This is python example on the Multiple Inheritance

class Father:
    pass

class Mother:
    pass


class Child(Father,Mother):
    pass

print(help(Child))


class Child2(Mother, Father):
    pass

print(help(Child2))