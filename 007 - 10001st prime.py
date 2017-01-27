__author__ = 'Mathias'

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

print(get_x_prime(10001))