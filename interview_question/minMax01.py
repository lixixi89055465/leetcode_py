'''

'''

import heapq


class Solution:
    def minMax(self, a, k, x):
        a = [-i for i in a]
        heapq.heapify(a)
        while k:
            k -= 1
            b = heapq.heappop(a)
            b += x
            heapq.heappush(a, b)
        b=heapq.heappop(a)
        return -b


solve = Solution()
a = [7, 2, 1]
k = 3
x = 2
result = solve.minMax(a, k, x)
print(result)
