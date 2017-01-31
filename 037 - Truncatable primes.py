__author__ = 'Mathias'

import timeit


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


def is_truncatable(prime, set):
    truncatable = True

    left_string = str(prime)[1:]
    while len(left_string) > 0:
        if {int(left_string)} <= set:
            left_string = left_string[1:]
        else:
            truncatable = False
            break

    right_string = str(prime)[:-1]
    while truncatable and len(right_string) > 0:
        if {int(right_string)} <= set:
            right_string = right_string[:-1]
        else:
            truncatable = False
            break

    return truncatable


start = timeit.default_timer()

primes_list = list(primes_sieve(1000000))
primes_set = set(primes_list)
truncatable_primes = []
while len(truncatable_primes) < 11:
    for prime in primes_list:
        if prime > 10 and is_truncatable(prime, primes_set):
            truncatable_primes.append(prime)

print(sum(truncatable_primes))
print(timeit.default_timer() - start)
