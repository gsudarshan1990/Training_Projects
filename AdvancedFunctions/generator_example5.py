"""
This is used to create the infinite sequence generator which can be iterator through the for loop
"""

def generate_power_of_two():
    """
    This is used to create a generator
    :return:
    """
    num = 0
    while True:
        num = num+1
        yield 2**num

g = generate_power_of_two()
count = 0
for p in g:
    print(p)
    count = count+1
    if count >20:
        break