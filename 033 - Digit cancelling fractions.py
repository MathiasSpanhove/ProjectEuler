__author__ = 'Mathias'

from fractions import Fraction
import timeit


def calc_cancelling_frac():
    for n in range(12, 100):
        if n % 10 == 0 or n % 11 == 0:
            continue
        for d in range(n + 1, 100):
            if d % 10 == 0 or d % 11 == 0:
                continue
            else:
                set_n = set(str(n))
                set_d = set(str(d))
                duplicate = (set_n & set_d)
                remaining = (set_n | set_d) - duplicate
                if len(remaining) == 2 and Fraction(n, d) == Fraction(int(list(set_n - duplicate)[0]),
                                                                      int(list(set_d - duplicate)[0])):
                    yield [n, d]


start = timeit.default_timer()

product = 1
for frac in list(calc_cancelling_frac()):
    product *= Fraction(frac[0], frac[1])

print(product.denominator)

print(timeit.default_timer() - start)
