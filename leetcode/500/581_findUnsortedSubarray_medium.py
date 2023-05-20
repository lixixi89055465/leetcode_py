'''
581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，
那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。



示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：

输入：nums = [1,2,3,4]
输出：0
示例 3：

输入：nums = [1]
输出：0


提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105

'''


class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        minI = 0
        maxL = len(nums)
        tnums = sorted(nums)
        minV = tnums[0]
        maxV = tnums[maxL - 1]
        while maxL:
            if nums[minI] == tnums[minI]:
                minI += 1
                maxL -= 1
                if maxL == 0:
                    return 0
                # minV = min(nums[minI:minI + maxL])
            elif nums[minI + maxL - 1] == tnums[minI + maxL - 1]:
                maxL -= 1
                if maxL == 0:
                    return 0
                # maxV = max(nums[minI:minI + maxL])
            else:
                break
        return maxL


solve = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1, 2, 3, 4]
# nums = [1]
# nums = [1, 3, 2, 4, 5]
result = solve.findUnsortedSubarray(nums)
print(result)
