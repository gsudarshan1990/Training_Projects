"""
This is an example of the class with polymorphism
"""

class Person:
    """This class describes a person"""
    def __init__(self, name, age):
        """This is used to initialize the values """
        self.name = name
        self.age = age

    def show_salary(self):
        print('Salary of the person notknown')

class AssistantProfessor(Person):
    """This class describes about Assistant Professor which forms a is a relationship with Person"""
    def __init__(self, name, age, salary):
        """This is used to initialize the values"""
        super().__init__(name, age)
        self.salary = salary

    def show_salary(self):
        print(" salary of the person %s is %d"%(self.name,self.age))

class Professor(Person):
    """This class describes about the Professor which forms a is a relationship with Person"""
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def show_salary(self):
        print(f"salary of the person {self.name} is {self.salary} ")

if __name__ == '__main__':
    p = Person('Jack',34)
    p.show_salary()
    ap = AssistantProfessor('Jim',46,26000)
    ap.show_salary()
    p = Professor('Jack',34,30000)
    p.show_salary()