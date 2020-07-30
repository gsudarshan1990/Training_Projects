"""
This is another example of assert

The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.

"""

def mysum(list1):
    if list1 == None:
        list1 =[]
        return len(list1)
    else:
        sum = 0
        for element in list1:
            sum = sum+element
        return sum

assert mysum([1,3,6]) == 10
assert mysum([]) == 0