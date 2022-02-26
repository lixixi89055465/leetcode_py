'''
229. 求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。





示例 1：

输入：[3,2,3]
输出：[3]
示例 2：

输入：nums = [1]
输出：[1]
示例 3：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]


提示：

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109


进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
'''


class Solution:
    def majorityElement(self, nums):
        n1 = float('inf')
        n2 = float('inf')
        n1m = 0
        n2m = 0
        for i in nums:
            if n1 == i:
                n1m += 1
            elif n2 == i:
                n2m += 1
            else:
                if n1m == 0:
                    n1 = i
                    n1m = 1
                elif n2m == 0:
                    n2 = i
                    n2m = 1
                else:
                    n1m -= 1
                    n2m -= 1
        n1m,n2m=0,0
        for i in nums:
            if i==n1:
                n1m+=1
            elif i==n2:
                n2m+=1
        ans=[]
        if n1m>len(nums)//3:
            ans.append(n1)
        if n2m>len(nums)//3:
            ans.append(n2)
        return ans



solve = Solution()
# nums = [3, 2, 3]
# nums = [1, 1, 1, 3, 3, 2, 2, 2]
nums = [1]
result = solve.majorityElement(nums)
print(result)
