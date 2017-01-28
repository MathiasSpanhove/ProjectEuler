__author__ = 'Mathias'

import timeit


def fibonacci(bound):
    init = [1, 1]
    index = 2
    while True:
        init = [init[1], init[0] + init[1]]
        index += 1

        if len(str(init[1])) >= bound:
            return index


start = timeit.default_timer()
print(fibonacci(1000))
print(timeit.default_timer() - start)
