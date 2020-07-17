"""
This is another example of collections and is to namedtuple
"""

from collections import namedtuple
Person = namedtuple('Person','name age gender')
Person = Person(name ='John', age = 29 , gender = 'M')
print(Person)


Car = namedtuple('Car', 'color model mileage')
Car = Car(color='red', model='tesla', mileage=10)
print(Car)