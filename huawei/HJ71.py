exp = 'te?t*.*'
str = 'txt12.xls'

# exp = '?*Bc*?'.lower()
# str = 'abcd'

# exp = 'p*p*qp**pq*p**p***ppq'
# str = 'pppppppqppqqppqppppqqqppqppqpqqqppqpqpppqpppqpqqqpqqp'

# exp = 'h*?*a'
# str = 'h#a'
# exp = '**Z'
# str = '0QZz'
# exp = '*h'
# str = 'h'


exp = 't?t*1*.*'
str = 'txt12.xls'


# exp = 'h'
# str = 'hh'


# def process(str, exp, si, ei):
#     if ei == len(exp):
#         return True if si == len(str) else False
#
#     if si > len(str) - 1:
#         return False
#     if exp[ei] != '*':
#         return (str[si] == exp[ei] or exp[ei] == '?' and (str[si].isalpha() or str[si].isalnum())) and process(str, exp,
#                                                                                                                si + 1,
#                                                                                                                ei + 1)
#     else:
#         ei += 1
#         while si < len(str) and (str[si].isalpha() or str[si].isalnum()):
#             if process(str, exp, si, ei):
#                 return True
#             si += 1
#         return True if process(str, exp, si, ei) else False


def dp(str, exp):
    lens = len(str)
    lene = len(exp)
    dp = [[False for i in range(lens + 1)] for _ in range(lene + 1)]
    for i in range(lens):
        dp[lene][i] = False
    for j in range(lene):
        dp[j][lens] = False
    dp[lene][lens] = True

    for i in range(lene - 1, -1, -1):
        for j in range(lens - 1, -1, -1):
            if exp[i] != '*':
                dp[i][j] = (str[j] == exp[i] or exp[i] == '?' and (str[j].isalpha() or str[j].isalnum())) and dp[i + 1][
                    j + 1]
            else:
                dp[i][j] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j + 1]) and (str[j].isalpha() or str[j].isalnum())
    return dp[0][0]


exp = input()
str = input()
str = str.lower()
exp = exp.lower()
while '**' in exp:
    exp = exp.replace('**', '*')

print('true' if dp(str, exp) else 'false')
