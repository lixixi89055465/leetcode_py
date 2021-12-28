'''
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0
        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float('-inf')
        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

        return max(sell[n - 1])


solve = Solution()
# k = 2
# prices = [3, 2, 6, 5, 0, 3]
# k = 2
# prices = [2,4,1]
# k = 1
# prices = [1]
# k = 2
# prices = [2, 2, 5]
# k = 1
# prices = [3, 3]
k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
k = 2
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
# k = 2
# prices = [1, 3, 5, 4, 3, 7, 6, 9, 2, 4]
k = 2
prices = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
# k = 2
# prices = [0, 8, 5, 7, 4, 7]
# k = 5
# prices = [1, 4, 7, 5, 6, 2, 5, 1, 9, 7, 9, 7, 0, 6, 8]
result = solve.maxProfit(k, prices)
print(result)
