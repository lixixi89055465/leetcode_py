'''
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

'''


class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        index = -1
        while left <=right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if index < 0:
            return 0
        count = 1
        left, right = index-1, index+1
        while left >=0:
            if nums[left] != target:
                break
            count += 1
            left -= 1
        while right < len(nums):
            if nums[right] != target:
                break
            count += 1
            right += 1
        return count


solve = Solution()
# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# nums = [1]
# target = 1
nums = [1,1,2]
target = 1
result = solve.search(nums, target)
print(result)
