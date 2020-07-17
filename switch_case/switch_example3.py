"""
This is the third example of switch
"""

character= {
    'a' : 'This is the first letter',
    'b' : 'This is the second letter',
    'z' : 'This is the last letter'
}

def explaining_switch_with_dict_existence(character2):
    if character2 in character:
        something = character[character2]
    else:
        something ='This is some other letter'
    return something

print(explaining_switch_with_dict_existence('a'))
print(explaining_switch_with_dict_existence('b'))
print(explaining_switch_with_dict_existence('c'))
print(explaining_switch_with_dict_existence('z'))