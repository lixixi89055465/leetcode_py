'''
1449. 数位成本和为目标值的最大数字
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。



示例 1：

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
示例 2：

输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
示例 3：

输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
示例 4：

输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"
'''


def concat(a, b, k):
    if a == "":
        return str(b) * k
    for i in range(len(a)):
        if a[i] < str(b):
            return a[:i] + str(b) * k + a[i:]
    return a + str(b) * k


def maxC(c1, c2):
    if len(c1) > len(c2):
        return c1
    elif len(c1) < len(c2):
        return c2
    if c1 > c2:
        return c1
    return c2


class Solution:

    def largestNumber(self, cost: list, target: int) -> str:
        dp = [['\0' for _ in range(target + 1)] for _ in range(len(cost) + 1)]
        for i in range(len(cost) + 1):
            dp[i][0] = ""
        for i in range(1, len(cost) + 1):
            for j in range(1, target + 1):
                if j < cost[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # print(dp[i - 1][target - cost[i]], i)
                    # dp[i][j] = max([maxC(dp[i - 1][j], concat(dp[i - 1][j - (k + 1) * cost[i]], i, k + 1)) for k in
                    #                 range(0, j // cost[i] + 1)])
                    for k in range(j // cost[i - 1]):
                        if dp[i - 1][j - (k + 1) * cost[i - 1]] != "\0":
                            dp[i][j] = maxC(dp[i][j], concat(dp[i - 1][j - (k + 1) * cost[i - 1]], i, k + 1))
                dp[i][j] = maxC(dp[i - 1][j], dp[i][j])
            print(dp[i])
        if dp[-1][-1] == "\0":
            return "0"
        return dp[-1][-1]


solve = Solution()
# cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
# target = 9
# cost = [7, 6, 5, 5, 5, 6, 8, 7, 8]
# target = 12
# cost = [2, 4, 6, 2, 4, 6, 4, 4, 4]
# target = 5
# cost = [6, 10, 15, 40, 40, 40, 40, 40, 40]
# target = 47
# cost = [1, 1, 1, 1, 1, 1, 1, 1, 1]
# target = 5000
cost = [5, 4, 4, 5, 5, 5, 5, 5, 5]
target = 29
result = solve.largestNumber(cost, target)
print(result)
