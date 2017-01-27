__author__ = 'Mathias'

import functools
import timeit

def get_prime(bound):
    primes = [2]
    n = 3

    yield 2
    while n <= bound:
        is_prime = True
        for x in primes:
            if (n % x == 0):
                is_prime = False
                break
        if (is_prime):
            primes.append(n)
            yield n
        n += 2


def calc_prime_factors(number):
    prime_generator = get_prime(number/2)
    while number != 1:
        prime = next(prime_generator)
        while (number % prime == 0):
            yield prime
            number = number / prime


def prime_factor(number):
    factorization = list(calc_prime_factors(number))
    if not factorization:
        return number
    return factorization


def smallest_multiple(number):
    array = []
    for i in range(2, number):
        primes = prime_factor(i)
        if type(primes) is int:
            if primes in array:
                array.remove(primes)
            else:
                array.append(primes)
        else:
            for j in primes:
                if j in array:
                    array.remove(j)
            for k in primes:
                array.append(k)
    return functools.reduce(lambda x, y: x*y, array)


start = timeit.default_timer()
print(smallest_multiple(20))
print(timeit.default_timer() - start)
