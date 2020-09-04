#This is python progam on classes


class Member:
    '''This class describes about a person'''
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


new_guy = Member('rahul','bose')
print(new_guy.firstname)
print(new_guy.lastname)

print(type(new_guy))
print(type(Member))
print(new_guy.__dict__)
