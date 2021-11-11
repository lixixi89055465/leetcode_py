maT = [
    [0, -2, -7, 0, 3],
    [9, 2, -6, 2, 5],
    [- 4, 1, -4, 1, 6],
    [- 1, 8, 0, -2, 2]
]
m = 4
n = 5
s = [0 for _ in range(n)]
for i in range(m):
    for j in range(n):
        if j == 0:
            s[j] = maT[i][j]
        else:
            s[j] += s[j - 1] + maT[i][j]

