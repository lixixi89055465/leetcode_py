def dpC(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for i in range(len2 + 1)] for _ in range(len1 + 1)]
    for i in range(len1 + 1):
        dp[i][0] = i
    for i in range(len2 + 1):
        dp[0][i] = i

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    print(dp[len1][len2])


s1 = input()
s2 = input()
# s1 = 'ucyfsmg'
# s2 = 'zuixhuhyjgksyhqkjqxwylkoubykjxtcvkyqjpzgltbemmbmqibxxqpkgbvwbmjotixanvciibubglizmumcrjavakiygyuv'
# s1 = 'abcdefae'
# s2 = 'adedea'
dpC(s1, s2)
