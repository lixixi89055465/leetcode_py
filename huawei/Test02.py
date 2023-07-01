a = list(input().lower())
b = list(input().lower())

dp = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
dp[0][0] = True
for i in range(1, len(a) + 1):
    dp[i][0] = dp[i - 1][0] and a[i - 1] == '*'
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        dp[0][j] = False
        if a[i - 1] != '*':
            if a[i - 1] == b[j - 1] and (a[i - 1] == '?' and b[j - 1].isalnum()):
                dp[i][j] = dp[i - 1][j - 1]
        elif a[i - 1] == '*':
            dp[i][j] = dp[i - 1][j] and (b[j - 1].isalnum() and dp[i][j - 1])
if dp[len(a)][len(b)]:
    print('true')
else:
    print('false')
