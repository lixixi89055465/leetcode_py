mima = input()
lenmima = len(mima)
dp = [[False for i in range(lenmima + 1)] for _ in range(lenmima + 1)]
for i in range(0, lenmima - 2):
    dp[i][i] = True
    dp[i][i + 1] = True if mima[i] == mima[i + 1] else False

dp[lenmima - 1][lenmima - 1] = True
dp[lenmima - 2][lenmima - 1] = True if mima[lenmima - 2] == mima[lenmima - 1] else False
res = 1
for i in range(3, lenmima + 1):
    for j in range(0, lenmima + 1 - i):
        dp[j][j + i - 1] = dp[j + 1][j + i - 2] if mima[j] == mima[j + i - 1] else False
        res = max(res, i if dp[j][j + i - 1] else 0)
print(res)
