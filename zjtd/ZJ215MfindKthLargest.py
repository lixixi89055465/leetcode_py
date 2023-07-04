import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


solution = Solution()
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(solution.findKthLargest(nums, k))
