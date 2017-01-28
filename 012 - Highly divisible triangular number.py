__author__ = 'Mathias'

import math
import timeit
import functools
from itertools import takewhile


def triangular():
    number = 1
    count = 2
    yield number
    while True:
        number += count
        yield number
        count += 1


def calc_divisors(n):
    step = 2 if n % 2 else 1
    return set(
        functools.reduce(list.__add__, ([i, n // i] for i in range(1, int(math.sqrt(n)) + 1, step) if n % i == 0)))


start = timeit.default_timer()
list = list(x for x in takewhile(lambda x: len(calc_divisors(x)) <= 500, triangular()))
print(list[-1] + len(list) + 1)
print(timeit.default_timer() - start)
