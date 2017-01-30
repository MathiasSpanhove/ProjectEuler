__author__ = 'Mathias'

import timeit


def calc_cycle(number):
    cycle = [1]
    pointer = 0
    limit = 0
    for i in range(number * 2):
        cycle.append(int((cycle[-1] * 10) % number))
        if cycle[-1] == cycle[pointer]:
            pointer += 1
            if limit == 0:
                limit = len(cycle) - 1
        else:
            pointer = 0
            limit = 0

        if pointer > 0 and pointer == limit:
            return limit

    return 0


start = timeit.default_timer()

largest_cycle = 0
number = 0
for i in range(1, 1000):
    cycle_length = calc_cycle(i)
    if cycle_length > largest_cycle:
        largest_cycle = cycle_length
        number = i

print(number)
print(timeit.default_timer() - start)
