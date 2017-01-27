__author__ = 'Mathias'

import timeit

def get_x_prime(number):
    primes = [2]
    n = 3
    count = 1

    while count < number:
        is_prime = True
        for x in primes:
            if (n % x == 0):
                is_prime = False
                break
        if (is_prime):
            primes.append(n)
            count += 1
        n += 2
    return primes[-1]


start = timeit.default_timer()
print(get_x_prime(10001))
print(timeit.default_timer() - start)
