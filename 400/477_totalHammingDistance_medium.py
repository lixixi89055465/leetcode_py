class Solution:
    def totalHammingDistance(self, nums):
        len1 = len(nums)
        bitNum = [0 for _ in range(32)]
        result=0
        for i in range(32):
            for n in nums:
                bitNum[i] += ((n >> i)&1)
            result+=(len1-bitNum[i])*bitNum[i]
        return result



a = [4, 14, 2]
solve = Solution()
result = solve.totalHammingDistance(a)
print(result)
