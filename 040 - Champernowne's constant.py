__author__ = 'Mathias'

import functools
import timeit
from math import log10


def integer_length(number):
    return int(log10(number)) + 1


def endless_counter():
    n = 1
    while True:
        yield n
        n += 1


def champernowne():
    d_max = 1000000
    counter = 0
    generator = endless_counter()
    checkpoint = 1  # 1,10,100,...

    while counter < d_max:
        next_number = next(generator)
        counter += integer_length(next_number)

        if counter >= checkpoint:
            index = counter - checkpoint
            yield str(next_number)[integer_length(next_number) - 1 - index]
            checkpoint *= 10


start = timeit.default_timer()
print(functools.reduce(lambda x, y: x * y, map(int, champernowne())))
print(timeit.default_timer() - start)
