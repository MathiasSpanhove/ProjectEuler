__author__ = 'Mathias'

import math
import timeit

number_list = set("123456789")


def calc_multiplicand_and_multiplier(number):
    step = 2 if number % 2 else 1
    for i in range(1 + step, int(math.sqrt(number)) + 1, step):
        if number % i == 0:
            yield [i, number // i]


def check_pandigital(string):
    return len(set(string) - number_list) == 0


start = timeit.default_timer()

pandigital_product_set = set()
for i in range(10000):
    i_string = str(i)
    mm_list = list(calc_multiplicand_and_multiplier(i))
    for tupel in mm_list:
        string = str(tupel[0]) + str(tupel[1]) + i_string
        if len(set(string)) == 9 and check_pandigital(string):
            pandigital_product_set.add(i)

print(sum(pandigital_product_set))

print(timeit.default_timer() - start)
