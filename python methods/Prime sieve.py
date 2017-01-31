__author__ = 'Mathias'


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
