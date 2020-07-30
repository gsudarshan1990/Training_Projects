"""
This is the another example of the assert statement.

L should be a list of numbers (ints or floats). The return value should be the maximum absolute value of the numbers in L
"""

def max_abs(L):
    """ This returns the maximum value """
    if L is None:
        return
    else:
        return max(L,key=abs)



assert max_abs([-2,3,-9,4,-12,7]) == -12

#Testing of the sorted and sort function

assert sorted([3,5,2,12]) == [2,3,5,12]

L = [9,3,7,4,2]
L.sort()

assert L== [2,3,4,7,9]