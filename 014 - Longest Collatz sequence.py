__author__ = 'Mathias'

import timeit

c = {}

def visualize_collatz_chain(number):
    yield number
    while number != 1:
        if (number % 2 == 0):
            number = number / 2
        else:
            number = 3*number + 1
        yield int(number)


def collatz_chain_length(number):
    number = int(number)
    if number == 1:
        c[number] = 1
        return 1
    if number in c:
        return c.get(number)
    else:
        if (number % 2 == 0):
            c[number] = 1 + collatz_chain_length(number / 2)
        else:
            c[number] = 1 + collatz_chain_length(3*number + 1)
        return c[number]


def search_longest_chain(number):
    longest_length = 0
    chain_number = 0

    for i in range(1, number):
        if i not in c:
            length = collatz_chain_length(i)
            if (length > longest_length):
                longest_length = length
                chain_number = i

    return [longest_length, chain_number]


start = timeit.default_timer()
print(search_longest_chain(1000000))
print(timeit.default_timer() - start)
