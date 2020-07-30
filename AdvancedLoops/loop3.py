"""
This specifies the usage of the pass block
"""

for letter in 'string':
    if letter == 'r':
        pass
    print(letter)

for letter in 'string':
    if letter == 'r':
        pass
        print('This is pass block')
    else:
        print('Current letter is:',letter)
print('Out of the loop')

print('Another Example of the pass block')

for i in range(10):
    if i%2 == 0:
        pass
    else:
        print(i)

print('='*20)
print('One more example of the pass block')

print('*'*20)

odd_count = 0
total_count = 0

for i in range(10):
    if i%2 == 0:
        pass
    else:
        odd_count+=1
    total_count+=1
    print('odd_count',odd_count)
    print('total_count',total_count)

print("Another Usage of the pass")

my_string=input('Enter the string')

digits = 0
letters = 0

print(len(my_string))
for letter in my_string:
    if letter.isdigit():
        digits+=1
    elif letter.isalpha():
        letters+=1
    else:
        pass
print('digits:',digits)
print('letters',letters)