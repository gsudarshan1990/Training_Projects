"""
This is the second example of switch using the dictionary
"""

character1 ={

    'a' : 'This is the first letter',
    'b' : 'This is the second letter',
    'z' : 'This is the las letter'
}

def explaining_switch_with_dict(character):
    """
    This is the function explains the switch using the dictionary
    :param character: arg1 and string1
    :return: string
    """
    something = character1.get(character,"This is someother letter")
    return something

print(explaining_switch_with_dict('a'))
print(explaining_switch_with_dict('m'))
print(explaining_switch_with_dict('z'))
print(explaining_switch_with_dict('b'))

