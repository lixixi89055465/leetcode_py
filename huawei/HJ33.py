ip = input()
convertIp = int(input())
ips = ip.split('.')
res = 0
base = 1
for p in ips[::-1]:
    res += (int(p) * base)
    base *= 256
print(res)
from collections import deque

ips = deque([])
while convertIp > 0:
    ips.appendleft(convertIp % 256)
    convertIp //= 256;
print('.'.join([str(i) for i in ips]))
