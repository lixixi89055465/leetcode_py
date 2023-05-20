'''
611. 有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

'''


class Solution:
    def triangleNumber(self, nums: list) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            k = i + 1
            for j in range(i + 1, len(nums) - 1):
                while k+1 < len(nums) and nums[i] + nums[j] > nums[k+1]:
                    k += 1
                result += max(k - j, 0)
        return result


solve = Solution()
nums = [2, 2, 3, 4]
result = solve.triangleNumber(nums)
print(result)
