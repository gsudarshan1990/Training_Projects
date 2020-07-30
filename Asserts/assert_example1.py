"""
This is an example of different type of assert
"""



assert type(9//5) == int
#assert type(9.0//5) == int

lst = ['a','b','c']

first_type = type(lst[0])
for element in lst:
    assert type(element) == first_type

lst2 = ['a','b','c',17]
first_type = type(lst[0])
"""
for element in lst2:
    assert type(element) == first_type
"""

lst =['a','b','c']
assert len(lst) < 10

nums = [1,5,8]
accum = 0
for w in nums:
    accum = accum+w
assert accum == 14

"""
nums  = []
accum = 0
for w in nums:
    accum = accum+w
assert accum == None
"""

nums = []

if len(nums) == 0:
    accum = None
else:
    accum = 0
    for w in nums:
        accum = accum+w
assert accum == None