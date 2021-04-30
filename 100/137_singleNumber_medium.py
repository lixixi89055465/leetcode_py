'''
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

 

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def singleNumber(self, nums: list) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += ((num >> i) & 1)
            if count % 3:
                if i == 31:
                    result-= (1 << i)
                else:
                    result|= (1 << i)

        return result


solve = Solution()
nums = [0, 1, 0, 1, 0, 1, 99]
nums = [2, 3, 2, 2]
nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
result = solve.singleNumber(nums)
print(result)
