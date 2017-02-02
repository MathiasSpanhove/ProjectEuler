__author__ = 'Mathias'

import timeit


def triangle():
    n = 286
    while True:
        yield int(n * (n + 1) / 2)
        n += 1


def pentagonal():
    n = 166
    while True:
        yield int(n * (3 * n - 1) / 2)
        n += 1


def hexagonal():
    n = 144
    while True:
        yield int(n * (2 * n - 1))
        n += 1


def find_triangle():
    triangle_gen = triangle()
    pentagonal_gen = pentagonal()
    hexagonal_gen = hexagonal()

    pentagonal_set = set()
    hexagonal_set = set()

    largest_penta = next(pentagonal_gen)
    largest_hexa = next(hexagonal_gen)

    pentagonal_set.add(largest_penta)
    hexagonal_set.add(largest_hexa)

    while True:
        next_triangle = next(triangle_gen)

        while next_triangle > largest_penta:
            largest_penta = next(pentagonal_gen)
            pentagonal_set.add(largest_penta)

        while next_triangle > largest_hexa:
            largest_hexa = next(hexagonal_gen)
            hexagonal_set.add(largest_hexa)

        if next_triangle in pentagonal_set and next_triangle in hexagonal_set:
            return next_triangle


start = timeit.default_timer()
print(find_triangle())
print(timeit.default_timer() - start)
