__author__ = 'Mathias'

import timeit

sumsquare = sum(list(map(lambda x: x**2, range(1,101))))
squaresum = sum(list(map(lambda x: x, range(1,101))))**2

start = timeit.default_timer()
print(squaresum - sumsquare)
print(timeit.default_timer() - start)
