"""
This is another example of the generator

Description of the Generator:
In python every sequence is iterable with the help of the iterator. This can be done with the help of the next() builtin function
Generator is used create a iterator for a sequence. This generator is a function which does not return but yields. Calling the generator obtains
the generator object and calling the next() function on the generator object provides the result

"""

def generator():
    n  = 1
    print('One!')
    yield n

    n = n+1
    print('Two !')
    yield n

    n = n+1
    print('Three !')
    yield n

    n = n+1
    print('four !')
    yield n

g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))