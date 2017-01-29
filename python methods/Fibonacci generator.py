__author__ = 'Mathias'


def fibonacci(bound):
    init = [1, 1]
    total = 0
    while True:
        init = [init[1], init[0] + init[1]]

        if init[1] < bound and init[1] % 2 == 0:
            yield init[1]
        elif init[1] > bound:
            break
