__author__ = 'Mathias'

import timeit


def double_base_palindroom(bound):
    for number in range(bound):
        if str(number) == str(number)[::-1]:
            binary = str(bin(number))[2:]
            if str(binary) == str(binary)[::-1]:
                yield number


start = timeit.default_timer()
print(sum(double_base_palindroom(1000000)))
print(timeit.default_timer() - start)
