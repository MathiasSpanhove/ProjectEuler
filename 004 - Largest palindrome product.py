__author__ = 'Mathias'

def largest_palindrome():
    x = 999
    palindroom = 0

    while x * 999 > palindroom:
        for y in reversed(range(100,999)):
            number = x*y
            if (number < palindroom):
                break
            elif (str(number) == str(number)[::-1]):
                palindroom = number
                break
        x -= 1

    return palindroom

print(largest_palindrome())