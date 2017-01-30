__author__ = 'Mathias'

import timeit


def distinct_power(a, b):
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            yield i ** j


start = timeit.default_timer()
print(len(set(distinct_power(100, 100))))
print(timeit.default_timer() - start)
