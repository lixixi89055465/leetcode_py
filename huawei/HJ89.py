import sys

m = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}


def process01(list):
    res = []
    for e in list:
        tmp = process01(list.remove(e))
        for t in tmp:
            t = e + t;
        res.append(tmp)
    return res


fu = ['+', '-', '*', '/']


def process(arr):
    list = []
    for e in arr:
        list.append(m[e])
    ans = process01(list)
    res=[]
    for l in ans:
        for f1 in fu:
            for f2 in fu:
                for f3 in fu:
                    if f1.equ



print('start')

for line in sys.stdin:
    a = line.split()
    print('0' * 100)

    for i in a:
        if len(i) > 2:
            print('ERROR')
            exit(0)
    process(a)
