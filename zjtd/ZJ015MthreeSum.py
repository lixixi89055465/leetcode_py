class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = []
        i = 0
        while i < n:
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left + 1] and left + 1 < right:
                        left += 1
                    left += 1
                    while nums[right] == nums[right - 1] and right - 1 > left:
                        right -= 1
                    right -= 1

                elif sum < 0:
                    left += 1
                else:
                    right -= 1
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans


solve = Solution()
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0, 0]
nums = [1,-1,-1,0]

print(solve.threeSum(nums))
