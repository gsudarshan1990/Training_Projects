"""
This is the first example of switch
"""

def explaining_switch(character):
    """
    This explains the switch
    :param character: arg1 and string
    :return: string
    """
    something =""
    if character == "a":
        something='This is the first letter'
    elif character == "b":
        something="This is second letter"
    elif character == 'z':
        something = 'This is the last letter'
    else:
        something ="This is some other letter"
    return (character+":"+something)

print(explaining_switch('a'))
print(explaining_switch('b'))
print(explaining_switch('m'))
print(explaining_switch('z'))