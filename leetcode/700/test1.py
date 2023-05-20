from collections import Counter

import heapq


class Solution:
    def minMax(self, a, k: int, x: int) -> int:
        b = [-i for i in a]
        heapq.heapify(b)
        for _ in range(k):
            c = -heapq.heappop(b)
            c -= x
            heapq.heappush(b,-c)
        result=heapq.heappop(b)
        return -result


a = [7, 2, 1]
k = 3
x = 2
solve = Solution()
reslt = solve.minMax(a, k, x)
print(reslt)
