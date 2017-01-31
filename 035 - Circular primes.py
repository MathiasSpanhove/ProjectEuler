__author__ = 'Mathias'

from collections import deque
import timeit


def calc_circular_perms(number):
    g = deque(list(str(number)))

    for i in range(len(g)):
        yield int(''.join(map(str, list(g))))
        g.rotate(1)  # for right rotation
        # or g.rotate(-1) for left rotation


def primes_sieve(bound):
    if bound == 0 or bound == 1:
        return 0

    a = [True] * bound
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for index in range(i * i, bound, i):
                a[index] = False


def calc_circular_primes(bound):
    checked = [False] * bound
    primes = set(primes_sieve(bound))

    for prime in primes:
        if checked[prime]:
            continue
        else:
            perms = set(calc_circular_perms(prime))
            if perms <= primes:
                for perm in perms:
                    yield perm
                    checked[perm] = True
            else:
                for perm in perms:
                    checked[perm] = True


start = timeit.default_timer()
print(len(list(calc_circular_primes(1000000))))
print(timeit.default_timer() - start)
