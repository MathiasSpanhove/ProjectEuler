__author__ = 'Mathias'

import timeit

start = timeit.default_timer()
print(sum(filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(1, 1000))))
print(timeit.default_timer() - start)
