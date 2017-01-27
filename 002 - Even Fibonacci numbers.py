__author__ = 'Mathias'

import timeit

#fib = lambda n: functools.reduce(lambda x: [x[1], x[0] + x[1]], range(n), [1, 1])[0]


def fibonacci(bound):
    init = [1, 1]
    total = 0
    while True:
        init = [init[1], init[0] + init[1]]

        if init[1] < bound and init[1] % 2 == 0:
            yield init[1]
        elif init[1] > bound:
            break


start = timeit.default_timer()
print(sum(x for x in fibonacci(4000000)))
print((timeit.default_timer() - start))
