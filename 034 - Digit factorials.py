__author__ = 'Mathias'

from math import factorial
import timeit


def calc_digit_factorials():
    for i in range(3, 100000):
        list = map(int, str(i))

        if (sum(map(lambda x: factorial(x), list))) == i:
            yield i


start = timeit.default_timer()
print(sum(calc_digit_factorials()))
print(timeit.default_timer() - start)
