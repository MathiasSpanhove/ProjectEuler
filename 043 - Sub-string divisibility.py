__author__ = 'Mathias'

import itertools
import timeit


def substring_divisibility():
    prime = [1, 2, 3, 5, 7, 11, 13, 17]
    perms = itertools.permutations("0123456789")

    for perm in perms:
        perm = str(''.join(perm))
        has_property = True
        for i in range(1, 8):
            d = perm[i:i + 3]
            if int(d) % prime[i] == 0:
                continue
            else:
                has_property = False
                break
        if has_property:
            yield int(perm)


start = timeit.default_timer()
print(sum(substring_divisibility()))
print(timeit.default_timer() - start)
