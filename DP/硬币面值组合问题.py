'''
问题描述
　　假设我们有8种不同面值的硬币｛1，2，5，10，20，50，100，200｝，用这些硬币组合够成一个给定的数值n。例如n=200，
那么一种可能的组合方式为 200 = 3 * 1 + 1＊2 + 1＊5 + 2＊20 + 1 * 50 + 1 * 100. 问总过有多少种可能的组合方式？
'''


def dpCoin(coins, n):
    dp = [[0 for _ in range(n + 1)] for _ in coins]
    # dp[0] = 1
    for i in range(len(coins)):
        for j in range(i, n, 1):
            if j % coins[i] == 0:
                dp[i][j] += 1
            for k in range(0, n, coins[i]):
                dp[i][j] = dp[i][j] + dp[i - 1][j - k] + 1
    return dp[n]


def select_coin(coin_value, total_value):
    min_coin_num = [0]
    for i in range(1, total_value + 1):
        min_coin_num.append(float('inf'))
        for value in coin_value:
            if value <= i and min_coin_num[i - value] + 1 < min_coin_num[i]:
                min_coin_num[i] = min_coin_num[i - value] + 1
    return min_coin_num


# coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = [1, 2, 5, 10]
# n = 200
n = 20
result = dpCoin(coins, n)
print(result)
