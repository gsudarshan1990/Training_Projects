"""
This is an exmaple of the closure which will be called with different parameters
"""

import random

def greet_the_person(greet,name):
    """
    This is the outer function
    :param greet: arg1 and the message with which greetings should be performed
    :param name: arg2 and name of the person
    :return: inner function object
    """
    annotations =['-','+','*',':','^']
    annotation_type = random.choice(annotations)

    def actual_greet():
        """
        This is the actual greet
        :return: Nothing
        """
        print(annotation_type*50)
        print(greet,name)
        print(annotation_type*50)
    return actual_greet

greet_greg_fn = greet_the_person('Good Evening!','Greg')
greet_james_fn = greet_the_person('Good Morning!','James')
greet_johnson_fn = greet_the_person('Hello!','Johnson')

greet_greg_fn()
greet_james_fn()
greet_johnson_fn()