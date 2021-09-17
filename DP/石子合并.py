'''
描述
    有N堆石子排成一排，每堆石子有一定的数量。现要将N堆石子并成为一堆。合并的过程只能每次将相邻的两堆石子堆成一堆，每次合并花费的代价为这两堆石子的和，
    经过N-1次合并后成为一堆。求出总的代价最小值。

输入
有多组测试数据，输入到文件结束。
每组测试数据第一行有一个整数n，表示有n堆石子。
接下来的一行有n（0< n <200）个数，分别表示这n堆石子的数目，用空格隔开
输出
输出总代价的最小值，占单独的一行
样例输入
3
1 2 3
7
13 7 8 16 21 4 18
样例输出
9
239
'''


def hebing(dp, start, end):
    # if start + 1 == end:
    #     dp[start][end] = dp[start][start] + dp[end][end]
    for i in range(start, end):
        if dp[start][i] <= 0:
            hebing(dp, start, i)
        if dp[i + 1][end] <= 0:
            hebing(dp, i + 1, end)
        if dp[start][end] == 0:
            dp[start][end] = dp[start][i] + dp[i + 1][end] + s[end] - s[start - 1]
        else:
            dp[start][end] = min(dp[start][end], dp[start][i] + dp[i + 1][end] + s[end] - s[start - 1])
        print(dp[start][end])


n = 7
arr = [13, 7, 8, 16, 21, 4, 18]
s = []
s.append(0)
for i in arr:
    s.append(s[-1] + i)

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     dp[i][i] = arr[i - 1]
hebing(dp, 1, n)

print(dp)
