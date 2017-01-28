__author__ = 'Mathias'

import math
import timeit

start = timeit.default_timer()
print(sum(map(lambda x: int(x), list(str(math.factorial(100))))))
print(timeit.default_timer() - start)
