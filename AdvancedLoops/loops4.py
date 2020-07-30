"""
This is another for loop example

1. Write a for loop which iterates over a random list of numbers  prints them except if divisible by 7 stops if 315 is encountered
list1= [124,145,173,231,256,301,315,361,399]

2. Here is the list of numbers list1 =[2,3,6,7,8,11,12,13,17,18] and use list comprehensions to generate cubes of numbers from the numbers
in the original list  only if the number is divisible by 3
"""

list_1 = [124,145,173,231,256,301,315,361,399]

for num in list_1:
    if num == 315:
        break
    if num%7 == 0:
        continue
    print(num,end=' ')


list2 = [2,3,6,7,8,11,12,13,17,18]

list3 = [num**3 for num in list2 if num%3 == 0]
print(list3)