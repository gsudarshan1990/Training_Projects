"""
This is another example of the for loop usage of the continue block
"""

word = 'string'
for letter in word:
    if letter == 'i':
        continue
    print(letter)
print('The end')

my_string = 'Students'

for letter in my_string:
    if (letter == 'e' or letter == 's'):
        continue
    else:
        print(letter)

for i in range(1,10):
    if i%2  == 0:
        print('%d is even number'%i)
    else:
        continue

print('Another form of the even number')
for num in range(1,10):
    if num%2 == 0:
        print('%d is found to be even number'%num)
    continue

print("="*20)

for i in range(1,12):
    print('Before the contine statement %d', i)
    if i%3 == 0:
        continue
    print('After the continue statement %d', i)

num_days = [31, 28,31,30,31,30,31,31,30,31,30,31]
months = ['Jan','Feb','March','April','May','June','July','August','September','October','November','December']

new_dict = dict()

for i,j in zip(months,num_days):
    new_dict.update({i:j})
    if new_dict[i]<29:
        continue
    else:
        print(i,'month',new_dict[i],'days')

animals = ['Deer','Rabbit','Lion','Dog','Cat','Elephant','Giraffe']

for pet in animals:
    if pet == 'Lion':
        continue
    if pet == 'Elephant':
        break
    print(pet)