'''
952. 按公因数计算最大组件大小
给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
返回 图中最大连通组件的大小 。



示例 1：



输入：nums = [4,6,15,35]
输出：4
示例 2：



输入：nums = [20,50,9,63]
输出：2
示例 3：



输入：nums = [2,3,6,7,4,12,21,39]
输出：8


提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
nums 中所有值都 不同
'''

from collections import defaultdict


class Solution:
    def getPrime(self, maxNum):
        primeSet = [2, 3]
        for i in range(4, maxNum + 1):
            flag = True
            for p in primeSet:
                if i % p == 0:
                    flag = False
                    break
            if flag:
                primeSet.append(i)
        return primeSet

    def largestComponentSize(self, nums):
        maxNum = max(nums)
        primeSet = self.getPrime(maxNum)
        m = defaultdict(list)
        pSetMap=defaultdict(set)
        for i in nums:
            flag = True
            pSet=set()
            for j in primeSet:
                if j > i:
                    break
                if i % j == 0:
                    pSet.add(j)
            pSetMap[i]=pSet
        visited=[False]*len(nums)
        result=[]
        numsList=[]
        for i in range(len(nums)):
            if visited[i]==False:
                flag=True
                for r in result:
                    if pSetMap[i].intersection(set(r)):
                        r.append(pSetMap[i])
                        flag=False
                        break
                if flag:
                    s=set([pSetMap[i]])
                    result.append(pSetMap(i))


        return result












solve = Solution()
nums = [2, 3, 6, 7, 4, 12, 21, 39]
result = solve.largestComponentSize(nums)
print(result)
