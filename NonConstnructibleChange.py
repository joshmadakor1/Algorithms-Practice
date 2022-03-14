'''
    Non-Constructible Change:
    Given an array of coins of different values, return the
    minimum amount of change that you will not be able to construct.

    Time:  O(NlogN), where N are the number of coins in the array
    Space: O(1)

    Last Practice: 2022-03-14 08:32:50
'''
def nonConstructibleChange(coins):
    coins.sort()
    sum = 0
    for coin in coins:
        if coin > sum + 1: return sum + 1
        sum += coin
    return sum + 1
