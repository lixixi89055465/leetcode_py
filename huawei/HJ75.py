def dp(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [0 if s1[i] != s2[0] else 1 for i in range(len1)]
    res = 0
    for i in range(len2):
        for j in range(len1 - 1, -1, -1):
            if j == 0:
                dp[j] = 1 if s1[0] == s2[i] else 0
            else:
                dp[j] = dp[j - 1] + 1 if s1[j] == s2[i] else 0
            res = max(res, dp[j])
    return res

s1=input()
s2=input()
print(dp(s1, s2))



