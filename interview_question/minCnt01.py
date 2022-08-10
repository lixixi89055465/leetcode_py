'''

'''


class Solution:
    def minCnt(self, s: str) -> int:
        result=0
        for ch in s[::-1]:
            if ch=='1':
                result+=1
        return result-1


solve = Solution()
s = "111"
s="1010"

result = solve.minCnt(s)
print(result)
