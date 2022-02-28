'''
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。



示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4


提示：

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
'''


class Solution:

    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

    def maxHeapify(self, nums, i, heapSize):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i
        if l < heapSize and nums[l] > nums[largest]:
            largest = l
        if r < heapSize and nums[r] > nums[largest]:
            largest = r
        if i != largest:
            self.swap(nums, i, largest)
            self.maxHeapify(nums, largest, heapSize)

    def buildHeap(self, nums, heapSize):
        for i in range(heapSize // 2, -1, -1):
            self.maxHeapify(nums, i, heapSize)

    def findKthLargest(self, nums, k):
        heapSize = len(nums)
        self.buildHeap(nums, heapSize)
        for i in range(heapSize - 1, heapSize - k, -1):
            self.swap(nums, 0, i)
            heapSize -= 1
            self.maxHeapify(nums, 0, heapSize)
        return nums[0]


solve = Solution()
nums = [1, 3, 1, 5, 100]
k = 2
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
result = solve.findKthLargest(nums, k)
print(result)
