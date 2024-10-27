# -*- coding: utf-8 -*-
# @Time : 2024/10/27 9:10
# @Author : nanji
# @Site : 
# @File : 3180maxTotalReward.py
# @Software: PyCharm 
# @Comment :
'''
3180. 执行操作可获得的最大总奖励 I
中等
相关标签
相关企业
提示
给你一个整数数组 rewardValues，长度为 n，代表奖励的值。

最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：

从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
以整数形式返回执行最优操作能够获得的 最大 总奖励。



示例 1：

输入：rewardValues = [1,1,3,3]

输出：4

解释：

依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。

示例 2：

输入：rewardValues = [1,6,4,3,2]

输出：11

解释：

依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。



提示：

1 <= rewardValues.length <= 2000
1 <= rewardValues[i] <= 2000
'''


class Solution(object):
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()
        m = rewardValues[-1]
        dp = [0] * (2 * m)
        dp[0] = 1
        for x in rewardValues:
            for k in range(2 * x - 1, x - 1, -1):
                if dp[k - x] == 1:
                    dp[k] = 1
        res = 0
        for i in range(len(dp)):
            if dp[i] == 1:
                res = i
        return res


rewardValues = [1, 6, 4, 3, 2]
s = Solution()
res = s.maxTotalReward(rewardValues)
print(res)
