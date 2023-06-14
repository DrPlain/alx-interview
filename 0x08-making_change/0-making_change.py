#!/usr/bin/python3
""" Algorithm
"""


def makeChange(coins, total):
    """ Determine the fewest number of coins needed
    to meet a given amount `total`
    """
    if total <= 0:
        return 0

    # Create a list `min_coins` to store the minimum number of coins
    # needed to attain each value from 0 - total
    # Initialize the list with positive infinity as plachlders
    min_coins = [float('inf')] * (total + 1)

    # Minimum number of coins needed to make a total of 0 is 0
    min_coins[0] = 0

    for coin in coins:
        # Update the minimum number of coins needed for
        # each total value starting from current coin
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if type(min_coins[total]) == int:
        return min_coins[total]
    return -1
