__author__ = 'Mathias'

import timeit


def search_bound(power):
    limit = 1
    while len(str((9 ** power) * limit)) > limit:
        limit += 1
    return limit


def power_digits(power):
    limit = search_bound(power)

    for n in range(2, int("9" * limit)):
        number = str(n).zfill(limit)
        if sum(map(lambda x: int(x) ** power, list(number))) == int(number):
            yield int(number)


start = timeit.default_timer()
print(sum(power_digits(5)))
print(timeit.default_timer() - start)
