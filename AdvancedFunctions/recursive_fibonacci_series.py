"""
This is the representation of the fibonacci series in the recursive format
"""

def fibonacci_series(number, fib_series):
    """
    This is the fibonacci series in the recurssive format
    :param number: arg1 and number of the iterations
    :param fib_series: list
    :return: nothing
    """
    if number < 2:
        return
    if fib_series == []:
        return
    l = len(fib_series)
    new_number = fib_series[l-1]+fib_series[l-2]
    fib_series.append(new_number)
    fibonacci_series(number-1,fib_series)

series = [0,1]
fibonacci_series(4, series)
print(series)

series =[0,1]
fibonacci_series(10,series)
print(series)