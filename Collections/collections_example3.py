"""
This is example of named tuple
"""

from collections import namedtuple

Person = namedtuple('Person','name age gender')
Person = Person(name ='John', age= 29 , gender='M')
print(Person)

Country = namedtuple('Country','Continent country capital')
Country1 = Country(Continent='Asia' , country='India' , capital='Delhi')
Country2 = Country(Continent ='Europe', country = 'Spain' , capital='madrid')
print(Country1)
print(Country2)

home = namedtuple('home','address location state')
home = home(address ='10', location='kakinad', state ='Ap')
print(home)