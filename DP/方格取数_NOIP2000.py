'''

'''
n = 8
inarr = [
    [2, 3, 13],
    [2, 6, 6],
    [3, 5, 7],
    [4, 4, 14],
    [5, 2, 21],
    [5, 6, 4],
    [6, 3, 15],
    [7, 2, 14]
]

arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for item in inarr:
    arr[item[0]][item[1]] = item[2]

dp = [[[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            for m in range(1, n + 1):
                dp[i][j][k][m] = max(
                    dp[i - 1][j][k - 1][m],
                    dp[i - 1][j][k][m - 1],
                    dp[i][j - 1][k - 1][m],
                    dp[i][j - 1][k][m - 1]
                ) + arr[i][j]
                if i != k and j != m:
                    dp[i][j][k][m] += arr[k][m]
print(dp[n][n][n][n])
