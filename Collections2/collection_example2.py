"""
This is example of deque

"""

from collections import deque
list1 = [1,2,3,4,5,6]

d = deque(list1)
d.append(7)
d.append(8)
d.append(9)
d.append(10)
d.appendleft(-1)
d.appendleft(-2)
d.appendleft(-3)
d.appendleft(-4)
d.appendleft(-5)

print(d)
print(d.pop())
print(d.popleft())
d.reverse()
print(d)

print(d.remove(3))
print(d)