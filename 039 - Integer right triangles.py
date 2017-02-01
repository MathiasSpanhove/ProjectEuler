__author__ = 'Mathias'

import timeit
from math import sqrt


def right_angle_triangle(perimeter):
    p = [0] * (perimeter + 1)
    for a in range(1, perimeter // 3 + 1):
        for b in range(a, perimeter - a):
            c = int(sqrt(a * a + b * b))
            if a * a + b * b == c * c and a + b + c <= perimeter:
                p[a + b + c] += 1
    return p


start = timeit.default_timer()
print(max([x, index] for index, x in enumerate(right_angle_triangle(1000)))[1])
print(timeit.default_timer() - start)
