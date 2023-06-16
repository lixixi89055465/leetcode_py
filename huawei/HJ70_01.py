n = input()
names = [chr(i) for i in range(ord('a', ord('z') + 1))]
matrix = dict()
for i in range(n):
    matrix[names[i]] = [int(x) for x in input().strip().split(' ')]
formula = input().strip()

cals = []
res = 0
for s in formula:
    if s.isalpha():
        cals.append(matrix[s])
    elif s == ')':
        new = [cals[-2][0], cals[-1][1]]
        res += cals[-2][0] * cals[-1][0] * cals[-1][1]
        cals.pop()
        cals[-1] = new.copy()
print(res)
