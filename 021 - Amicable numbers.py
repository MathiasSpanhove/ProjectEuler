__author__ = 'Mathias'

import functools
import math
import timeit


def calc_divisors(n):
    step = 2 if n % 2 else 1
    return set(
        functools.reduce(list.__add__, ([i, n // i] for i in range(1, int(math.sqrt(n)) + 1, step) if n % i == 0)))


start = timeit.default_timer()

total = 0
for i in range(1, 10000):
    a = sum(calc_divisors(i)) - i  # minus i because we only want proper divisors
    if a > i:
        if sum(calc_divisors(a)) - a == i:
            total += a + i

print(total)
print(timeit.default_timer() - start)
