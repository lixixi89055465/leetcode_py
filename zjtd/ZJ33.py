'''
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1


提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        nlen = len(nums)
        k = self.findK(nums, 0, nlen - 1)
        left, right = k, (k - 1) % nlen
        while (left - k) % nlen < (right - k) % nlen:
            mid = (left + ((right - left + nlen) % nlen) // 2) % nlen
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = (mid + 1) % nlen
        return left if nums[left] == target else -1

    def findK(self, nums, left, right):
        while left < right:
            if nums[left] < nums[right]:
                return left
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return left


solve = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# target = 3
# nums = [1]
# target = 1
# nums = [1, 3]
# target = 3
# nums = [3, 1]
# target = 1
print(solve.search(nums, target))
