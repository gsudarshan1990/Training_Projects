"""
This is an example of the for loop with tuple and dictionary
"""

dogs = ("pug",'doberman','golden retriever')

for dog in dogs:
    print("A breed of dog",dog)

print('*'*20)

dog_weight =(('pug',20),
             ('doberman',80),
             ('golden retriever',55)
)

for i, (dog,weight) in enumerate(dog_weight):
    print('The index is %d and dog is %s and weight is %d'%(i,dog,weight))

print('*'*20)

student_scores ={'John':80,'Sam':60,'Jill':50,'Bob':96}
for student in student_scores:
    print("Student",student,"score",student_scores[student])

print('key','*'*20)
print(student_scores.keys())

print('values','*'*20)
print(student_scores.values())

print('Usage of items')
for student,score in student_scores.items():
    print("Student",student,'score',score)