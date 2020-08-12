"""
This is another example of the class
"""
#Write a class named "Phone". The Phone class should
#have an attribute called "storage" which defaults to
#128, and an attribute called "color" which defaults
#to "red".
#
#Hint: 'attribute' is another common word for
#'instance variable'.


#Write your class here!

class Phone:
    """This represents the phone class"""
    def __init__(self):
        """This is used to initialize the values"""
        self.storage = 128
        self.color = 'red'

new_phone = Phone()
print(new_phone.storage)
print(new_phone.color)