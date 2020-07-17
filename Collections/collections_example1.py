"""
This is the first example related counter
"""

from collections import Counter

list_ = [1,2,1,3,5,6,7,8,9,10,1,3,5,6,3,7,8,2]
cnt = Counter()

for word in list_:
    cnt[word]+=1

print(cnt)

c = Counter({1:3,2:4})
print(list(c.elements()))

c1 = Counter({1:3, 2:4, 3:5})
c2 = Counter({1:2, 2:5, 3:3})
c1.subtract(c2)
print(c1)

list2 = [3,4,5,3,2,4,5,6,7,8,2,3,4,5,7]
cnt = Counter(list2)
print(cnt.most_common())