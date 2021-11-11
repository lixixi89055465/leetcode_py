'''
滑雪:Michael喜欢滑雪百这并不奇怪， 因为滑雪的确很刺激。
可是为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，
你不得不再次走上坡或者等待升降机来载你。
Michael想知道载一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字
代表点的高度。下面是一个例子
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。在上面的例子中，
一条可滑行的滑坡为24-17-16-1。当然25-24-23-...-3-2-1更长。事实上，这是最
长的一条。输入输入的第一行表示区域的行数R和列数C(1 <= R,C <= 100)。下面是R
行，每行有C个整数，代表高度h，0<=h<=10000。输出输出最长区域的长度。
输入：输入的第一行表示区域的行数R和列数C
(1 <= R,C <= 100)。下面是R行，每行有C个整数，代表高度h，0<=h<=10000。
输出：输出最长区域的长度。
样例输入
5 5
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
样例输出
25
'''

inputT = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]
r = 5
c = 5
a = {}
for i in range(r):
    for j in range(c):
        if a.keys().__contains__(inputT[i][j]) == False:
            a[inputT[i][j]] = []
        a[inputT[i][j]].append((i, j))

print(a)
print('1' * 10)
dp = [[0 for _ in range(c)] for _ in range(r)]
for i in sorted(a.keys()):
    arr = a[i]
    for j in arr:
        if j[0] == 0 and j[1] == 0:
            if inputT[j[0]][j[1]] > inputT[j[0] + 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)
        if j[0] == r-1 and j[1] == 0:
            if inputT[j[0]][j[1]] > inputT[j[0] - 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)
        if j[0] == 0 and j[1] == 0:
            if inputT[j[0]][j[1]] > inputT[j[0] + 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)
        if j[0] == 0 and j[1] == 0:
            if inputT[j[0]][j[1]] > inputT[j[0] + 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)


        if j[0] == 0 or j[0] == r - 1 or j[1] == 0 or j[1] == c - 1:
            if j[0] == 0 and inputT[j[0]][j[1]] > inputT[j[0]][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if j[0] == r - 1 and inputT[j[0]][j[1]] > inputT[j[0] - 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] - 1][j[1]] + 1)
            if j[1] == 0 and inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)
            if j[1] == c - 1 and inputT[j[0]][j[1]] > inputT[j[0]][j[1] - 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] - 1] + 1)
        else:
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] + 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0] - 1][j[1]]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0] - 1][j[1]] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] + 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] + 1] + 1)
            if inputT[j[0]][j[1]] > inputT[j[0]][j[1] - 1]:
                dp[j[0]][j[1]] = max(dp[j[0]][j[1]], dp[j[0]][j[1] - 1] + 1)

print(dp)
