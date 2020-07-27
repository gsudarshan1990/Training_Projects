"""
This is the example of the generator function

Description of the generator function
In python every sequence is iterable and with the help of the iterator. Iterator contains the builtin next() function.
Generator is used to create the iterator for the sequence and calling the generator creates the generator object. This object can be invoked
by the next() function
"""

def generator():
    print('One!')
    yield 1

    print('Two')
    yield 2

    print('Three')
    yield 3

    print('Four')
    yield 4

g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))