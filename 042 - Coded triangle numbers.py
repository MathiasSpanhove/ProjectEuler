__author__ = 'Mathias'

import string
import timeit

triangle_numbers = dict()
for index, triangle_nb in enumerate((0.5 * i * (i + 1) for i in range(200)), 1):
    triangle_numbers[triangle_nb] = index

values = dict()
for index, letter in enumerate(string.ascii_lowercase, 1):
    values[letter] = index

with open("text files/p042_words.txt") as f:
    content = f.read()
names = [x.strip('"').lower() for x in content.split(",")]

total = 0
for name in names:
    name_score = 0
    for letter in name:
        name_score += values[letter]
    if name_score in triangle_numbers:
        total += 1

start = timeit.default_timer()
print(total)
print(timeit.default_timer() - start)
