"""
This class represents the IntergerSet
"""

class intSet:
    """This class describes about the intset"""
    def __init__(self):
        """This is used to initialize the values"""
        self.vals = []

    def insert(self, e):
        """This is used to insert the value"""
        if type(e) == int:
            if not e in self.vals:
                self.vals.append(e)
        else:
            raise ValueError("Given Value cannot be added",e)

    def member(self, e):
        """This is used to check whether e exists or not in the set"""
        return e in self.vals

    def remove(self, e):
        """This is used to remove the value """
        try:
            self.vals.remove(e)
        except:
            raise ValueError("Interger not found")

    def __str__(self):
        self.vals.sort()
        result = ''
        for val in self.vals:
            result = result+str(val)+','
        return '{'+result[:-1]+'}'


s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
s.remove(3)
print(s)
s.insert('abc')
#s.remove(3)
