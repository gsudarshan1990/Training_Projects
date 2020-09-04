#This is another python program


class Student:
    '''This class describes about student'''
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
        self.clubs = set()
        self.active = True

    def set_name(self, name):
        self.__name = name

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def add_club(self, club_name):
        self.clubs.add(club_name)

    def remove_club(self, club_name):
        self.remove_club(club_name)

    def set_active(self, active_value):
        self.active = active_value

    def print_details(self):
        print('Student name:',self.__name)
        print('Student gpa ',self.__gpa,'student clubs',self.clubs,'active',self.active)

s1 = Student('James',3.9)
s1.add_club('yoga')
s1.print_details()
s1.add_club('Yoga')
s1.print_details()
s1.add_club('yoga')
s1.print_details()

