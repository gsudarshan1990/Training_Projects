"""
Difference between the class and dictionaries
"""

class Name:
    """This defines the name of the person"""
    def __init__(self):
        """This is used to initialize the names of the function"""
        self.firstname = "Johny"
        self.lastname = "Depp"

mynamedict = {'firstname':'Johny','lastname':'Depp'}

mynameinst = Name()

print(mynamedict['firstname'])
print(mynameinst.firstname)