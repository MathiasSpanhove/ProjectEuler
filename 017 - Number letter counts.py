__author__ = "Mathias"

import timeit

num2word = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 1000: "One Thousand"}


def number2word(number):
    if number in num2word:
        return num2word.get(number)

    if number < 100:
        return num2word.get(number - number % 10) + " " + num2word.get(number % 10)
    elif number % 100 == 0:
        return num2word.get((number - number % 100) / 100) + " Hundred"
    else:
        return num2word.get((number - number % 100) / 100) + " Hundred and " + \
               number2word(number - (number - number % 100))


start = timeit.default_timer()

total = 0
for i in range(1, 1001):
    total += sum(map(lambda x: len(x), number2word(i).split(" ")))
print(total)

print(timeit.default_timer() - start)
