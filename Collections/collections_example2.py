"""
This is example of deque
"""

from collections import deque
list2 = ['a','b','c','d']
d = deque(list2)
d.append('e')
d.append('f')
d.append('g')
d.append('h')
d.appendleft('-a')
d.appendleft('-b')
d.appendleft('-c')
d.appendleft('-d')
d.extend([1,2,3,4,5])
d.extendleft([-1,-2,-3,-4,-5])

print(d)
d.pop()
d.popleft()

print(d)

d.reverse()
print(d)
