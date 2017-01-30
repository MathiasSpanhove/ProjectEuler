__author__ = 'Mathias'

from itertools import permutations
import timeit

start = timeit.default_timer()

print(''.join(list(permutations("0123456789", 10))[999999]))

print(timeit.default_timer() - start)
