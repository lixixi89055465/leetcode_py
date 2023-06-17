str1 = input()
str2 = input()
# str1 = 'abcdefghijklmnop'
# str2 = 'abcsafjklmnopqrstuvw'

# s1 = 'nvlrzqcjltmrejybjeshffenvkeqtbsnlocoyaokdpuxutrsmcmoearsgttgyyucgzgcnurfbubgvbwpyslaeykqhaaveqxijc'
# s2 = 'wkigrnngxehuiwxrextitnmjykimyhcbxildpnmrfgcnevjyvwzwuzrwvlomnlogbptornsybimbtnyhlmfecscmojrxekqmj'

s1 = str2 if len(str1) > len(str2) else str1
s2 = str1 if len(str1) > len(str2) else str2
len1 = len(s1)
len2 = len(s2)
dp = [0 for i in range(len2)]

res = 0
resS = ''
for i in range(len1):
    for j in range(len2 - 1, 0, -1):
        dp[j] = max(dp[j], dp[j - 1] + 1) if s1[i] == s2[j] else 0
        if res <dp[j]:
            res = dp[j]
            resS = s1[i - res + 1: i + 1]

# print(res)
print(resS)
