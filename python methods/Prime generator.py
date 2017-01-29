__author__ = 'Mathias'


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
