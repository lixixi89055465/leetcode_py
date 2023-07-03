class Solution:
    def getTotalNum(self, cur, n):
        next = cur + 1
        totalNum = 0
        while cur <= n:
            totalNum += min(n - cur + 1, next - cur)
            next *= 10
            cur *= 10

        return totalNum

    def findKthNumber(self, n, m):
        m = m - 1
        cur = 1
        while m > 0:
            nodeNums = self.getTotalNum(cur, n)
            if nodeNums <= m:
                m -= nodeNums
                cur += 1
            else:
                m -= 1
                cur *= 10
        return cur


n = 13
m = 2
solution = Solution()
print(solution.findKthNumber(n, m))
