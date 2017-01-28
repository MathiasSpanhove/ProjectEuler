__author__ = 'Mathias'

import timeit


def spiral_generator(bound):
    total = 1
    yield total

    for i in range(1, bound + 1):
        for j in range(4):
            total += i * 2
            yield total


def spiral_sum(bound):
    curr = 1
    total = 1
    for i in range(1, bound + 1):
        for j in range(4):
            curr += i * 2
            total += curr
    return total


start = timeit.default_timer()
print(sum(list(spiral_generator(500))))
print(timeit.default_timer() - start)

start = timeit.default_timer()
print(spiral_sum(500))
print(timeit.default_timer() - start)
