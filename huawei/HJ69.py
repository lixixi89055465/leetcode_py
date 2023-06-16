x = int(input())
y = int(input())
z = int(input())

m1 = []
for i in range(x):
    m1.append([int(j) for j in input().split(' ')])

m2 = []
for i in range(y):
    m2.append([int(j) for j in input().split(' ')])
res = [[0 for i in range(z)] for _ in range(x)]

for i in range(x):
    for j in range(z):
        res[i][j] = 0
        for k in range(y):
            res[i][j] += m1[i][k] * m2[k][j]
for r in res:
    print(' '.join([str(i) for i in r]))
