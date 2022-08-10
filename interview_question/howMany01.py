'''

'''

from collections import Counter
class Solution:
    def howMany(self, S: str, k: int) -> int:
        m = Counter()
        for ch in S:
            m[ch] += 1
        result = 0
        for i in m:
            if m[i] >= k:
                result += 1
        return result


solve = Solution()
s = "aacbcbdefghijklmnopqrstuvwxyz"
k = 1
result = solve.howMany(s, k)
print(result)
