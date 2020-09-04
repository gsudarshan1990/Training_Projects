#This is python program on multiple Inheritance


class GrandParent:
    '''This class describes about the Grand Parent City'''
    def __init__(self, city):
        self.__city = city

    def get_city(self):
        return self.__city

class Parent(GrandParent):
    '''This class describes about the Parents Lastname'''
    def __init__(self, city, lastname):
        GrandParent.__init__(self, city)
        self.__lastname = lastname

    def get_lastname(self):
        return self.__lastname

class Person(Parent):
    '''This class describes about the Person'''
    def __init__(self, city, lastname, firstname):
        Parent.__init__(self, city , lastname)
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def get_introduction(self):
        last_name = super().get_lastname()
        city = super().get_city()
        print('%s is from %s'%(last_name,city))

    def get_information(self):
        last_name = super().get_lastname()
        firstname = self.get_firstname()
        city = super().get_city()
        print('%s %s from %s'%(firstname, last_name, city))

p1 = Person('Delhi','bose','rahul')

p1.get_information()
p1.get_introduction()