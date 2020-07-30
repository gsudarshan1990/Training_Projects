"""
Another set of example on range
"""

for i in range(1,11):
    if i %2 == 0:
        print('%d is even'%i)
    else:
        print('%d is odd'%i)

my_list2 = []

for i in range(1,35):
    if (i%3 ==0) or (i%5==0):
        my_list2.append(i)
print(my_list2)

print('*'*20)
items =[]

for i in range(100,301):
    num_str = str(i)
    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    third_digit = int(num_str[2])

    if (first_digit%2==0) and (second_digit%2 == 0) and (third_digit%2 ==0):
        items.append(num_str)
print(','.join(items))

"Below is the table printing"

print('Below is the table printing')

for num1 in range(1,10):
    print('num1',num1,end =' ')
    for num_2 in range(1,10):
        print('{:2d}'.format(num1*num_2),end=" ")
    print()