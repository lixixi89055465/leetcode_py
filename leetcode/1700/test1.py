import collections
import math
class Solution:
    def countPairs(self, deliciousness: list) -> int:
        Hash = collections.defaultdict(int)
        ans = 0
        Max = int(math.log2(max(deliciousness)))+2
        mod = 10**9 + 7
        def gethash(num):
            Sum = 0
            begin =  0 if num == 0 else int(math.log2(num))
            for i in range(begin,Max):
                if 2**i - num in Hash:
                    # print("num",num," Hash",2**i - num,"sum",Sum)
                    Sum += Hash[2**i - num]%mod
            return Sum%mod
        for i in deliciousness:
            temp = gethash(i)
            ans += temp
            ans %= mod
            Hash[i] += 1
        return ans%mod


solve = Solution()
# deliciousness = [1, 1, 1, 3, 3, 3, 7]
# deliciousness = [1, 3, 5, 7, 9]
# deliciousness = [32 for _ in range(300000)]
deliciousness = [32 for _ in range(300001)]
result = solve.countPairs(deliciousness)
print(result)
