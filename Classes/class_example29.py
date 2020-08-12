"""
This is another example of the class which elaborates on the type error

#Rewrite the "Number" class
#This time, however, require arguments for value and
#even in the constructor. Then, inside the constructor,
#create new instance variables called value and even that
#copy the values of the arguments passed into the
#constructor.
#
#Then, as before, create an instance of this class and
#assign it to a variable called "number_instance". value
#should again be set to 101 and even should be set to
#False.
#
#Hint: Remember, the way you initialize the instance will
#have to change, too, based on the changes to the
#constructor that we're requiring.
"""

class Number:
    """This class provides information related to integer and states whether it is even or not"""
    def __init__(self, value, even):
        """This is used to initialize the values"""
        self.value = value
        self.even = even

number_instance = Number(101, False)
#number_instance = Number() causes the TypeError

