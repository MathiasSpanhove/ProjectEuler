__author__ = 'Mathias'

import functools
import timeit

start = timeit.default_timer()
print(functools.reduce(lambda x, y: int(x) + int(y), list(str(2 ** 1000))))
print(timeit.default_timer() - start)
