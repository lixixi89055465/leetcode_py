# n, m = input().split()
# nlen = len(n)
# mlen = len(m)
# n, m = int(n), int(m)
n = 200
m = 125


def startn(k):
    base = 1
    sum = 0
    for i in range(k):
        sum += base;
        base *= 10
    return sum


nlen = len(str(n))
t = 0
scount = startn(nlen - t)
res = ""
k = 1
while scount < m:
    m -= scount
    k += 1
res = res+str(k)
if m == 1:
    print(res)

m -= 1
t+=1
scount = startn(nlen - t)
k = 0
while scount < m:
    m -= scount
    k += 1
res += str(k)
if m == 1:
    print(res)



m -= 1
t+=1
scount = startn(nlen - t)
k = 0
while scount < m:
    m -= scount
    k += 1
res += str(k)
print(res)


