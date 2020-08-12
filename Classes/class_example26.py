"""
This is another example of the class
"""

#Write a class named "Number" with one attribute called
#"value" which defaults to 0 and another attribute called
#"even" which defaults to True.
#
#Next, create an instance of this class and assign it to
#a variable called "number_instance".
#
#Then, set the value attribute to 101 and the even
#attribute to False.

class Number:
    """This class is used to represent the integer number and classify it as even or not"""
    def __init__(self):
        """This is used to initialize the values"""
        self.value = 0
        self.even = True

number_instance = Number()
number_instance.value=101
number_instance.even= False