# -*- coding: utf-8 -*-
# @Time : 2024/10/4 8:29
# @Author : nanji
# @Site : 
# @File : M1227nthPersonGetsNthSeat.py
# @Software: PyCharm 
# @Comment :1227. 飞机座位分配概率
# 中等
# 相关标签
# 相关企业
# 提示
# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
#
# 剩下的乘客将会：
#
# 如果他们自己的座位还空着，就坐到自己的座位上，
#
# 当他们自己的座位被占用时，随机选择其他座位
# 第 n 位乘客坐在自己的座位上的概率是多少？
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：1.00000
# 解释：第一个人只会坐在自己的位置上。
# 示例 2：
#
# 输入: n = 2
# 输出: 0.50000
# 解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
#
#
# 提示：
#
# 1 <= n <= 10^5
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # for i in range(1, n + 1):
        #     dp[i] = dp[i - 1] * 1 / i * (i - 2) + 1 / i
        # return dp[-1]
        if n == 1:
            return 1
        if n==2:
            return 0.5
        pre = 1
        cur = 0.5
        for i in range(3, n + 1):
            print(pre)
            tmp = cur
            cur = pre * 1 / i * (i - 2) + 1 / i
            pre = tmp
        return pre


s = Solution()
res = s.nthPersonGetsNthSeat(4)
# res = s.nthPersonGetsNthSeat(1)
# res = s.nthPersonGetsNthSeat(3)
# res = s.nthPersonGetsNthSeat(2)
print(res)
