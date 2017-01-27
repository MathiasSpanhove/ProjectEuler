__author__ = 'Mathias'

sumsquare = sum(list(map(lambda x: x**2, range(1,101))))
squaresum = sum(list(map(lambda x: x, range(1,101))))**2

print(squaresum - sumsquare)