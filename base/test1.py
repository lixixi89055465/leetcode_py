from collections import defaultdict
from collections import deque
from collections import Counter

s1 = "abcd"
s2 = "abce"

m1 = Counter()
m2 = Counter()
for ch in s1:
    m1[ch] += 1
for ch in s2:
    m2[ch] += 1
print(m1 - m2)
print(m2 - m1)
if len(m1-m2)==1 and len(m2-m1)==1:
    print('t')

