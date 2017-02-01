__author__ = 'Mathias'

from math import log10

def integer_length(number):
    return int(log10(number)) + 1
