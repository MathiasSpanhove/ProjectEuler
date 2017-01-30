__author__ = 'Mathias'

import timeit


def coin_sum(amount, coins):
    if amount == 0 or len(coins) == 1:
        return 1
    else:
        different_ways = 0
        coins = sorted(coins)
        largest_coin = coins[-1]
        ways = amount // largest_coin
        for n in range(ways + 1):
            different_ways += coin_sum(amount - largest_coin * n, coins[:-1])
        return different_ways


start = timeit.default_timer()
print(coin_sum(200, [1, 2, 5, 10, 20, 50, 100, 200]))
print(timeit.default_timer() - start)
