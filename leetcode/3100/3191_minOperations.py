# -*- coding: utf-8 -*-
# @Time : 2024/10/20 8:56
# @Author : nanji
# @Site : https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
# @File : 3191_minOperations.py
# @Software: PyCharm 
# @Comment :
'''

代码
测试用例
测试结果
测试结果
3191. 使二进制数组全部等于 1 的最少操作次数 I
中等
相关标签
相关企业
提示
给你一个二进制数组 nums 。

你可以对数组执行以下操作 任意 次（也可以 0 次）：

选择数组中 任意连续 3 个元素，并将它们 全部反转 。
反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。

请你返回将 nums 中所有元素变为 1 的 最少 操作次数。如果无法全部变成 1 ，返回 -1 。



示例 1：

输入：nums = [0,1,1,1,0,0]

输出：3

解释：
我们可以执行以下操作：

选择下标为 0 ，1 和 2 的元素并反转，得到 nums = [1,0,0,1,0,0] 。
选择下标为 1 ，2 和 3 的元素并反转，得到 nums = [1,1,1,0,0,0] 。
选择下标为 3 ，4 和 5 的元素并反转，得到 nums = [1,1,1,1,1,1] 。
示例 2：

输入：nums = [0,1,1,1]

输出：-1

解释：
无法将所有元素都变为 1 。



提示：

3 <= nums.length <= 105
0 <= nums[i] <= 1
'''


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrLen = len(nums)
        res = 0
        for i in range(arrLen - 2):
            if nums[i] == 0:
                res += 1
                nums[i + 1] = 0 if nums[i + 1] == 1 else 1
                nums[i + 2] = 0 if nums[i + 2] == 1 else 1
        if nums[arrLen - 1] == 0 or nums[arrLen - 2] == 0:
            return -1
        return res


# nums = [0, 1, 1, 1, 0, 0]
nums = [0,1,1,1]
s = Solution()
res = s.minOperations(nums)
print(res)
