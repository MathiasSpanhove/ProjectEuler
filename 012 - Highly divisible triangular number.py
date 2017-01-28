__author__ = 'Mathias'

import math
import timeit
from itertools import takewhile


def triangular():
    number = 1
    count = 2
    yield number
    while True:
        number += count
        yield number
        count += 1


def calc_divisors(number):
    divisors = [1, number]
    for x in range(2, math.ceil(math.sqrt(number))):
        if (number % x == 0):
            divisors.append(x)
            divisors.append(number / x)

    return divisors


start = timeit.default_timer()
list = list(x for x in takewhile(lambda x: len(calc_divisors(x)) <= 500, triangular()))
print(list[-1] + len(list) + 1)
print(timeit.default_timer() - start)
