"""
This is an example on range
"""

my_range = range(5)
print(my_range)

print(list(my_range))
print(tuple(my_range))

print(list(range(5,10)))
print(list(range(-5,5)))

"""
Float Object cannot be used in range

for i in range(3.3):
    print(i)
"""

"""
String Object cannot be used in range

for i in range('B','E'):
    print(i)
"""

for m in range(3):
    print('Hello')

for _ in range(3):
    print('Good')

for _ in range(2**3):
    print('Morning')

for number in range(5,10):
    print('number is %d ',number)

print('*'*20)
for i in range(5,8):
    print(i,'square is ',i**2)
print('End loop')

print('*'*20)
for i in range(5,10+2):
    print(i)

print('*'*20)

y = range(7)

for num in reversed(y):
    print(num)

print(list(range(5,10,2)))

print(list(range(10,2,-2)))
print(tuple(range(10,5,-2)))

print(list(range(-2,-10,-2)))

start = -2
stop = -10
step = -2

for number in range(start,stop,step):
    print(number)
