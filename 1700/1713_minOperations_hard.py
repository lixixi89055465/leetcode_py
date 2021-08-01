'''
1713. 得到子序列的最少操作次数
给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。

每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。

请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。

一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。



示例 1：

输入：target = [5,1,3], arr = [9,4,2,3,4]
输出：2
解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。
示例 2：

输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
输出：3


提示：

1 <= target.length, arr.length <= 105
1 <= target[i], arr[i] <= 109
target 不包含任何重复元素。
'''


class Solution:
    def minOperations(target, arr):
        # 获得下标数组 只需要包括存在target中的元素的下标
        indices = []
        dict_index = dict(zip(target, range(len(target))))
        for i in range(len(arr)):
            if arr[i] in dict_index:
                indices.append(dict_index[arr[i]])
        # 最长公共子序列的长度
        nums = indices
        len_lis = self.lengthOfLIS(indices)

        return len(target) - len_lis

    def lengthOfLIS(nums):
        # tails的最终结果:
        # tails[i]为nums中长度为(i+1)的递增子序列的末尾元素最小值
        # tails的中间状态，即遍历到nums[j]时tails的含义:
        # tails[i]表示nums[0,...,j]中长度为(i+1)的递增子序列的末尾元素最小值
        # tails的初始值=[nums[0]] (相当于j=0)
        tails = [nums[0]]
        for j in range(1, len(nums)):
            if nums[j] > tails[-1]:  # 延长tails长度
                tails.append(nums[j])
            elif nums[j] < tails[-1]:  # 不延长 但是更新最小值
                # 使用二分法获得 min{k | nums[j]<=tails[k]}
                # 使得tails[k-1]<nums[j]<=tails[k], 上面的<=保证了下方左侧的<，保证严格递增
                left, right = 0, len(tails) - 1
                # left<=mid<right
                while left < right:
                    mid = (left + right) // 2
                    if nums[j] <= tails[mid]:
                        right = mid
                    else:
                        left = mid + 1
                # k=left
                tails[left] = nums[j]
            print('nums[0..j]={} tails={}'.format(nums[0:j + 1], tails))
        return len(tails)

