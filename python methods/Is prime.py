__author__ = 'Mathias'

import math


def is_prime(n):
    return not (n < 2 or any(n % x == 0 for x in range(2, int(math.sqrt(n)) + 1)))
