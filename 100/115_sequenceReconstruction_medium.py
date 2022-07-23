'''
剑指 Offer II 115. 重建序列
给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。

例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。



示例 1：

输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
输出：false
解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
因为 nums 不是唯一最短的超序列，所以返回false。
示例 2：

输入：nums = [1,2,3], sequences = [[1,2]]
输出：false
解释：最短可能的超序列为 [1,2]。
序列 [1,2] 是它的子序列：[1,2]。
因为 nums 不是最短的超序列，所以返回false。
示例 3：

输入：nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
输出：true
解释：最短可能的超序列为[1,2,3]。
序列 [1,2] 是它的一个子序列：[1,2,3]。
序列 [1,3] 是它的一个子序列：[1,2,3]。
序列 [2,3] 是它的一个子序列：[1,2,3]。
因为 nums 是唯一最短的超序列，所以返回true。


提示：

n == nums.length
1 <= n <= 104
nums 是 [1, n] 范围内所有整数的排列
1 <= sequences.length <= 104
1 <= sequences[i].length <= 104
1 <= sum(sequences[i].length) <= 105
1 <= sequences[i][j] <= n
sequences 的所有数组都是 唯一 的
sequences[i] 是 nums 的一个子序列
'''
from collections import defaultdict, Counter


class Solution:
    def sequenceReconstruction(self, nums, sequences) -> bool:
        m = [[set() for i in range(2)] for _ in range(len(nums) + 1)]
        for i in sequences:
            for j, vj in enumerate(i):
                if j == 0:
                    m[vj][1] = m[vj][1].union(set(i[1:]))
                elif j == len(i) - 1:
                    m[vj][0] = m[vj][0].union(set(i[:-1]))
                else:
                    m[vj][1] = m[vj][1].union(set(i[j + 1:]))
                    m[vj][0] = m[vj][0].union(set(i[:j]))
        print(m)
        while True:
            flag=False
            for k,i in enumerate(m[1:]):
                # left
                if len(i[0])<k:
                    left = i[0]
                    for j in i[0]:
                        left= left.union(m[j][0])
                    if len(i[0])<len(left):
                        flag=True
                    i[0]=left
                #right
                if len(i[1])<k :
                    right=i[1]
                    for j in i[1]:
                        right=right.union(m[j][1])
                    if len(i[1])<len(right):
                        flag=True
                    i[1]=right
            if flag==False:
                break
        print(m)



solve = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
# sequences = [[1, 2, 3], [1, 3, 6], [6, 7], [3, 4, 5, 6]]
sequences = [[1, 2], [2, 3], [3, 4], [5, 6],[6,7],[4,5]]
result = solve.sequenceReconstruction(nums, sequences)
print(result)
