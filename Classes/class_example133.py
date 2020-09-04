#This is another python program


class Employee:
    '''This class describes about the employee'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print('name',self.name)

    def show_age(self):
        print('age',self.age)

class Salary:
    '''This class describes about the Salary'''
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

class Database(Employee,Salary):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age)
        Salary.__init__(self, salary)

d1 = Database('rahul',28,'30000')
d1.show_name()

print(help(Database))