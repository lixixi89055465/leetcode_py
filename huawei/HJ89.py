import sys

m = {'A': 1, 'B': '2', '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
     'K': 13}
reverse_m = {1: 'A', 2: '2', 11: 'J', 12: 'Q', 13: 'K'}


def process02(list, s, index):
    if index == 0:
        tmp = process02(list, list[0], 1)
        return [list[0]] + tmp if tmp != None else None
    if index == 4:
        return [] if s == 24 else None
    fu = ['+', '-', '*', '/']
    for f1 in fu:
        tmp = s
        if f1 == '+':
            tmp += list[index]
        elif f1 == '-':
            tmp -= list[index]
        elif f1 == '*':
            tmp *= list[index]
        else:
            tmp //= list[index]
        resArr = process02(list, tmp, index + 1)
        if resArr != None:
            resArr = [f1, list[index]] + resArr
            return resArr
    return None


def process01(list):
    res = []
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                for t in range(0, 4):
                    if i != j and i != k and i != t and j != k and j != t and k != t:
                        tmp = process02([list[i], list[j], list[k], list[t]], 0, 0)
                        if tmp != None:
                            return tmp
    return None


def process(arr):
    list = []
    for e in arr:
        if len(e) > 2:
            print('ERROR')
            return
        list.append(m[e])
    tmp = process01(list)
    if tmp != None:
        print(''.join(str(i) if i not in reverse_m else str(reverse_m[i]) for i in tmp))
    else:
        print('NONE')


# a = '4 2 K A'
for line in sys.stdin:
    a = line
    process(a.split())
# a = 'A A A A'
# a = 'B 5 joker 4'
