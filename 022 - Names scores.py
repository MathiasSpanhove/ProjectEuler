__author__ = 'Mathias'

import string
import timeit

values = dict()
for index, letter in enumerate(string.ascii_lowercase, 1):
    values[letter] = index

start = timeit.default_timer()

with open("text files/p022_names.txt") as f:
    content = f.read()
names = [x.strip('"').lower() for x in content.split(",")]
names.sort()

total_name_scores = 0
for index, name in enumerate(names, 1):
    name_score = 0
    for letter in name:
        name_score += values[letter]
    total_name_scores += name_score * index

print(total_name_scores)

print(timeit.default_timer() - start)
