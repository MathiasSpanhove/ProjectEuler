__author__ = 'Mathias'

import timeit


def formula(n, a, b):
    return n ** 2 + a * n + b


def primes_sieve(bound):
    if (bound == 0 or bound == 1):
        return 0

    a = [True] * bound
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for index in range(i * i, bound, i):
                a[index] = False


start = timeit.default_timer()

primes = set(primes_sieve(10000))
a_list = [x for x in range(-999, 999, 1)]
b_list = [x for x in range(-1000, 1000, 1)]
largest_n = 0
best_a = 0
best_b = 0

for a in a_list:
    for b in b_list:
        n = 0
        new_list = []
        new_list.append(formula(n, a, b))
        while len(set(new_list) - primes) == 0:
            new_list.append(formula(n, a, b))
            n += 1
        if n > largest_n:
            largest_n = n
            best_a = a
            best_b = b

print(largest_n, best_a, best_b, best_a * best_b)

print(timeit.default_timer() - start)
