s1 = input()
s2 = input()
# s1 = '9876543210'
# s2 = '1234567890'

long = s1 if len(s1) > len(s2) else s2
short = s2 if len(s1) > len(s2) else s1
lenL = len(long)
lenS = len(short)
jinwei = 0
res = ''
for i in range(1, lenL + 1):
    if i <= lenS:
        tmp = int(long[-i]) + int(short[-i]) + jinwei
    else:
        tmp = int(long[-i]) + jinwei
    res = str(tmp % 10) + res
    jinwei = 1 if tmp > 9 else 0
if jinwei == 1:
    res = '1' + res
print(res)
