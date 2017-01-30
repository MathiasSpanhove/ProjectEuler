__author__ = 'Mathias'

import timeit

total = 0
for i in range(1, 1001):
    total += i ** i

start = timeit.default_timer()
print(str(total)[-10:])
print(timeit.default_timer() - start)
