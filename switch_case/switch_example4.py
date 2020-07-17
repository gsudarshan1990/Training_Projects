"""
This is another example of switch using defaultdict
"""

character ={
    'a' : 'This is the first letter',
    'b' : 'This is the second letter',
    'z' : 'This is the last letter'
}

from collections import defaultdict

def explaining_switch_with_default_dict(character2):
    """
    This uses the default dict to explain the switch
    :param character2: arg1 and string1
    :return: string
    """
    character1 = defaultdict(lambda :'some other character',character)
    return character2+":"+character1[character2]

print(explaining_switch_with_default_dict('a'))
print(explaining_switch_with_default_dict('b'))
print(explaining_switch_with_default_dict('m'))
print(explaining_switch_with_default_dict('z'))