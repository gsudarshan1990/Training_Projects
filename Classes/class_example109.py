#This python program describes about the Class


class Student:
    name = ''
    score  = 0
    active = True

s1 = Student()


print((s1.name,s1.score,s1.active))

s1.name = 'john'
s1.score =50

print(s1.name,s1.score,s1.active)

s2 = Student()
print((s1.name,s2.score,s2.active))

s2.name ='lily'
print((s2.name,s2.score,s2.active))

s2.active = False
print((s2.name,s2.score,s2.active))