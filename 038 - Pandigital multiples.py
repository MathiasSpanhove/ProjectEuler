__author__ = 'Mathias'

import timeit

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def pandigital_multiples(bound):
    for i in range(1, bound):
        string = ""
        n = 1
        while len(string) < 9:
            string += str(i * n)
            n += 1
        if len(string) > 9:
            continue
        elif set(map(int, string)) >= digits:
            yield int(string)


start = timeit.default_timer()
print(max(pandigital_multiples(9999)))
print(timeit.default_timer() - start)
