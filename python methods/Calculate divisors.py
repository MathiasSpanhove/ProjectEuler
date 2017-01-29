__author__ = 'Mathias'

import functools
import math


def calc_divisors(number):
    step = 2 if number % 2 else 1
    return set(functools.reduce(list.__add__, ([i, number // i] for i in range(1, int(math.sqrt(number)) + 1, step)
                                               if number % i == 0)))
