"""
Control Statements on the for loops
"""

fruits = ['mango','orange','apple']
for fruit in fruits:
    if fruit == 'orange':
        print('Orange is present in the list')

numbers = [11,33,55,39,2,55,75,37,22,23,41,13]

for number in numbers:
    if number %2 == 0:
        print('The list contains the even number %d'%number)

print('*'*20)

years =[2016,2017,2018,2019,2020]

for year in years:
    if year%4 == 0:
        print('Year %d is a leap year'%year)
    else:
        print('Year %d is not a leap year'%year)

colors = ['Red','Green','Blue']
objects =['Pen','Marker','Book']

for color in colors:
    for object in objects:
        print(color," ",object)