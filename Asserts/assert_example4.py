"""
This is another example of the assert statement

The class Student is supposed to accept two arguments in its constructor:
A name string

An optional integer representing the number of years the student has been at Michigan (default:1)

Every student has three instance variables:
self.name (set to the name provided)

self.years_at_university

self.knowledge (initialized to 0)

There are three methods:
.study() should increase self.knowledge by 1 and return None

.getKnowledge() should return the value of self.knowledge

.year_at_university should return the value of self.year_at_university

"""

class Student:
    """
    This class represents the student at the University
    """
    def __init__(self, name, num_of_years_at_university=1):
        """
        This is used to initialize the values
        :param name: arg1 and name of the student
        :param num_of_years_at_university: arg2 and number of years at the university
        """
        self.name = name
        self.num_of_years_at_university = num_of_years_at_university
        self.knowledge = 0

    def study(self):
        """
        This represents the knowledge accumulated yesterday
        :return: returns Nothing
        """
        self.knowledge += 1
        return None

    def get_knowledge(self):
        return self.knowledge

    def year_at_university(self):
        return self.num_of_years_at_university


s1 = Student('jack',2)
assert s1.get_knowledge() == 0
s1.study()
assert s1.get_knowledge() == 1
assert s1.num_of_years_at_university == 2
s1.study()
assert s1.get_knowledge() == 2
