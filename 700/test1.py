from collections import Counter

s = "abCf"
a = Counter(filter(str.isalpha, s.lower()))
b = "abcd"
b = Counter(b)
print(not (b - a))
print(not (a - b))
