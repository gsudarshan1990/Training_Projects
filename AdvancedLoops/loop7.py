"""
This is another example of the for loop

"""

numbers =[4,6,9,10]

for num in numbers:
    quotient = num //2
    print(quotient,'quotient for the number',num,'/2')

mixed_list = [145,10.5,1+3j,True,'Python',(0,1),[2,-5],{'class':'v','section':'A'}]

print('*'*20)
for item in mixed_list:
    print('type:',type(item),'value',item)

values =[2,4,6,8]
square = 0

print('*'*20)
for value in values:
    square = value**2
    print('square of the number value %d is %d'%(value,square))

print('*'*20)
string1 = input('Enter the string')
count = 0

for letter in string1:
    count+=1
print(count)

print('*'*20)
numbers = [1,2,8,9,12]

for number in numbers:
    print(number)
else:
    print('No more items on the list')

print('*'*20)
characters =['a','b','c','d','e']

for character in characters:
    print(character)
else:
    print('All the characters has been printed')