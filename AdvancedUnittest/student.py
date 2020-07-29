"""
This represents the student file
"""

class Student:
    """
    This class describes about the student
    """
    stu_stipend_hike = 1.05

    def __init__(self, first, last, stipend):
        self.first = first
        self.last = last
        self.stipend = stipend

    @property
    def mail(self):
        return self.first+"."+self.last+"@xyz.com"

    @property
    def fullname(self):
        return self.first+" "+self.last

    def apply_hike_rate(self):
        self.stipend = int(self.stipend)*self.stu_stipend_hike