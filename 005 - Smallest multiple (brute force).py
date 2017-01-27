__author__ = 'Mathias'

import math

def smallest_mulitple(number):
    smallest = 0
    while True:
        found = True
        smallest += number
        for i in reversed(range(1, 20)):
            if (smallest % i != 0):
                found = False
                break
        if found:
            return smallest


print(smallest_mulitple(20))