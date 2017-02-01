__author__ = 'Mathias'

import timeit
from math import log10


def integer_length(number):
    return int(log10(number)) + 1


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


def calc_pandigital(prime_list):
    digits = {1}
    for prime in prime_list:
        length = integer_length(prime)
        if length > len(digits):
            digits.add(length)

        if set(map(int, str(prime))) >= digits:
            yield prime


start = timeit.default_timer()
primes = list(primes_sieve(10000000))
print(max(calc_pandigital(primes)))
print(timeit.default_timer() - start)
