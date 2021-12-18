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
        i = 0
        while i < len(prices) - 1:
            if prices[i] == prices[i + 1]:
                prices.pop(i)
            else:
                i += 1
        if not prices or len(prices) <= 1:
            return 0

        left = 0
        right = 0
        n = len(prices)
        i = 0
        ret = 0
        buys = []
        sells = []
        while i < n:
            while i < n - 1 and prices[i] == prices[i + 1]:
                i += 1
            if i == 0:
                if prices[i] < prices[i + 1]:
                    left = prices[i]
                    buys.append(left)
            elif i == n - 1:
                if prices[i] > prices[i - 1]:
                    right = prices[i]
                    sells.append(right)
                    ret += right - left

            elif prices[i] < prices[i + 1] and prices[i] < prices[i - 1]:
                left = prices[i]
                buys.append(left)
            elif prices[i] > prices[i + 1] and prices[i] > prices[i - 1]:
                right = prices[i]
                ret += right - left
                sells.append(right)
            i += 1
        # print(ret)
        # print(buys)
        # print(sells)
        maxK = len(buys)
        if maxK <= k:
            return sum(sells) - sum(buys)
        mk = len(buys)
        for k in range(k, mk):
            c = [j - i for i, j in zip(buys, sells)]
            mk = len(c)
            index = c.index(min(c))
            if index == mk - 1:
                if sells[-1] > sells[-2]:
                    sells.pop(-2)
                    buys.pop(-1)
                else:
                    sells.pop()
                    buys.pop()
            elif index == 0:
                if buys[0] < buys[1]:
                    sells.pop(0)
                    buys.pop(1)
                else:
                    buys.pop(0)
                    sells.pop(0)
            else:
                if sells[index] - sells[index - 1] <= sells[index] - buys[index] and sells[index + 1] - sells[index] <= \
                        sells[index] - buys[index]:
                    buys.pop(index)
                    sells.pop(index)
                elif sells[index] - sells[index - 1] < sells[index + 1] - sells[index]:
                    buys.pop(index + 1)
                    sells.pop(index)
                else:
                    buys.pop(index - 1)
                    sells.pop(index)


        return sum(sells) - sum(buys)

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
