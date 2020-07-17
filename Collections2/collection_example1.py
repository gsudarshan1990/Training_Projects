"""
This is about the counter
"""

list_ = [1,2,1,3,4,1,2,3,1,3,4,5,2,3,1]
from collections import Counter

cnt = Counter()
for word in list_:
    cnt[word]+=1

print(cnt)

c1 = Counter({1:3, 2:2, 3:1})
c2 = Counter({1:2, 2:1, 3:0})
c1.subtract(c2)
print(c1)

list2 = [1,2,1,2,3,4,5,2,1,2,3,5,3,2,1]
cnt2 = Counter(list2)
print(cnt2.most_common())

cnt3 =  Counter({1:3, 2:3, 3:6, 4:2})
print(list(cnt3.elements()))