"""
This is the example of the decorators

"""

def print_message():
    print('Yohoo! Decorators are cool')

import random

def highlight():
    annotations = ['+','-','*',':','^']
    annotation_type = random.choice(annotations)
    print(annotation_type*50)
    print_message()
    print(annotation_type*50)

#highlight()

def print_another_message():
    print('Do you know? decorators use closures')

#Here the print_another message cannot use the highlight

#We are defining the decorator (Decorator does not modify the codes it just decorators(i.e) adds the additional functionality

def make_hightlighted(func):
    annotations = ['+','-','*',':','^']
    annotations_type = random.choice(annotations)
    def highlight2():
        print(annotations_type*50)
        func()
        print(annotations_type*50)
    return highlight2

highlight_print_message = make_hightlighted(print_message)
highlight_print_message()

highlight_print_another_message = make_hightlighted(print_another_message)
highlight_print_another_message()

@make_hightlighted
def print_third_message():
    print('Now you will see how this message is highlighed')

print_third_message()

@make_hightlighted
def print_any_message():
    print('This is an important message and the result of this message should be highlighted')

print_any_message()