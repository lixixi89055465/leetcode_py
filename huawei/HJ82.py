def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def subtraction(a, b):
    (a, b) = (a, b) if a > b else (b, a)
    g = gcd(a, b)
    a, b = a // g, b // g
    res = []
    while b != 1:
        c = a // b + 1
        res.append(str(1) + str("/") + str(c))
        a, b = a * c, b * c - a
        g = gcd(a, b)
        a, b = a // g, b // g
    res.append(str(1) + str("/") + str(a))
    return '+'.join(res)


# print(gcd(15, 9))
# a, b = 15, 9
# ji = gcd(a, b)
# a, b = a // ji, b // ji
# print(a, b)
# print(subtraction(15, 9))
# print(subtraction(8, 11))
# fenshu = input()
# a, b = fenshu.split('/')
# print(subtraction(int(a), int(b)))


import sys

for line in sys.stdin:
    a = line.strip().split('/')
    res = '1/' + a[1] + '+'
    res *= int(a[0])
    print(res.strip('+'))
