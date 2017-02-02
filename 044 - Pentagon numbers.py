__author__ = 'Mathias'

import timeit


def calc_pentagonal():
    n = 1
    while True:
        yield int(n * (3 * n - 1) / 2)
        n += 1


def find_pair():
    found = False
    pentagonal_generator = calc_pentagonal()

    pentagonal_set = set()
    pentagonal_queue = []
    next_element = next(pentagonal_generator)
    largest_element = next_element
    pentagonal_set.add(next_element)

    while not found:

        if len(pentagonal_queue) == 0:
            next_element = next(pentagonal_generator)
        else:
            next_element = pentagonal_queue.pop(0)

        for pentagonal in pentagonal_set:
            add = next_element + pentagonal
            min = next_element - pentagonal

            if min in pentagonal_set:
                while add > largest_element:
                    new_element = next(pentagonal_generator)
                    largest_element = new_element
                    pentagonal_queue.append(new_element)

                if add in pentagonal_set or add in pentagonal_queue:
                    return [next_element, pentagonal]
            else:
                continue

        pentagonal_set.add(next_element)


start = timeit.default_timer()

pair = find_pair()
print(pair[0] - pair[1])

print(timeit.default_timer() - start)
