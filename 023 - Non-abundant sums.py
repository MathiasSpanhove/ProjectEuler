__author__ = 'Mathias'

import functools
import itertools
import math


def calc_divisors(number):
    step = 2 if number % 2 else 1
    return set(functools.reduce(list.__add__, ([i, number // i] for i in range(1, int(math.sqrt(number)) + 1, step)
                                               if number % i == 0)))


def is_abundant(number):
    return number < sum(calc_divisors(number)) - number


def calc_abundant(bound):
    curr = 2
    while curr <= bound:
        if is_abundant(curr):
            yield curr
        curr += 1


def calc_abundant_efficient(bound):
    a = [False] * (bound + 1)

    curr = 2
    while curr <= bound:
        if a[curr]:
            yield curr
        elif is_abundant(curr):
            a[curr] = True
            yield curr

            temp = curr * 2
            while temp < bound:
                a[temp] = True
                temp += temp
        curr += 1


def calc_non_abundant_sums():
    abundant_list = list(calc_abundant_efficient(28123))
    sums = sorted(set(sum(c) for c in itertools.combinations_with_replacement(abundant_list, 2)))
    print(sum(number for number in range(1, 28123) if number not in sums))


if __name__ == "__main__":
    import timeit

    setup = "from __main__ import calc_non_abundant_sums"
    print(min(list(timeit.Timer("calc_non_abundant_sums()", setup=setup).repeat(10, 1))))
