__author__ = 'Mathias'

import math
import timeit


def calc_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            if math.sqrt(a * a + b * b) == 1000 - a - b:
                return a * b * (1000 - a - b)


start = timeit.default_timer()
print(calc_pythagorean_triplet())
print(timeit.default_timer() - start)
