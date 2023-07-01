# n = 10
# s = 'UUUU'
n = int(input())
s = input()
cur = 0
curS = 0
if n <= 4:
    print(' '.join([str(i + 1) for i in range(n)]))
    for c in s:
        if c == 'U':
            cur = (cur - 1) % n
        else:
            cur = (cur + 1) % n
    print(cur + 1)
    exit(0)

for c in s:
    if c == 'U':
        curS = 0 if curS == 0 and cur > 0 and cur <= n - 4 else (curS - 1) % 4
        cur = (cur - 1) % n
    else:
        curS = 3 if curS == 3 and cur >= 3 and cur < n - 1 else (curS + 1) % 4
        cur = (cur + 1) % n
# print(curS)
res = ''
for i in range(cur - curS + 1, cur + 1):
    res += str(i) + ' '
for i in range(cur + 1, cur - curS + 5):
    res += str(i) + ' '
print(res)
print(cur + 1)
