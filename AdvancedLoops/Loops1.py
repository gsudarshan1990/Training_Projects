"""
This is used for advanced for loops
"""

for letter in 'python':
    if letter == 'o':
        break
    print(letter)

print('='*20)
print()
for letter in 'python':
    print(letter)
    if letter == 'o':
        break

def forwithelse(word):
    for letter in word:
        if letter == 'c':
            print('The letter is found', letter)
            break
    else:
        print('No Such letter exists')

forwithelse('icecream')
forwithelse('bad')


mylist = range(10)

for num in mylist:
    if num**2 > 20:
        break
    print(num,'square',num**2)

print('='*20)

places = ['New Zealand','Norway','Bostwana','Zimbabwe','Uzbeskistan','Paraguay']
villian_at = 'Mali'

for villian  in places:
    if villian == villian_at:
        print('Villan has been found')
else:
    print('Villian has been gotten away')

#Calculating the prime of the number

num = int(input('Enter the number to check whether it a prime number or not'))

for i in range(2,num//2):
    if num%i == 0:
        print('{} is not a prime number'.format(num))
        break
else:
    print('{} is a prime number'.format(num))

for i in range(3):
    password = input('Enter the password')
    if password == 'secret':
        print('Hurray! you guessed the correct password')
        break
else:
    print('All the 3 attempts of the password has been failed')