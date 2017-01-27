__author__ = 'Mathias'

import math

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


print(prime_factor(13195)[-1])
print(prime_factor(600851475143)[-1])
