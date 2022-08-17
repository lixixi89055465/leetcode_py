'''
768. 最多能完成排序的块 II
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
示例 2:

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
注意:

arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。
'''

import collections


class Solution:
    def maxChunksToSorted(self, arr):
        seqArr = sorted(arr)
        m = collections.defaultdict()
        for i, v in enumerate(arr):
            if v in m:
                m[v] = max(m[v], i)
            else:
                m[v] = i
        ans = list()
        start = 0
        for a in seqArr:
            position = m[a]
            if position >= start:
                # ans.append(arr[start: position + 1])
                tmpAns = arr[start: position + 1]
                minE = min(tmpAns)
                maxE = max(tmpAns)
                for i, v in enumerate(tmpAns):
                    if v != minE:
                        break
                    ans.append([v])
                if i!=0:
                    continue
                start = 0
                end = len(tmpAns)
                for i, v in enumerate(tmpAns[::-1]):
                    if v != maxE:
                        end = end - i
                        break
                if start < end:
                    ans.append(tmpAns[start:end])
                for i in tmpAns[max(start, end):]:
                    ans.append([i])
                start = position + 1
        print(ans)
        return len(ans)


solve = Solution()
# arr = [2, 1, 3, 4, 4]
arr = [3, 2, 1, 3, 4, 4]
arr = [3, 2, 1, 3, 3, 4, 4]
arr = [3, 2, 1, 3, 3, 4, 4, 6, 5]
arr = [3, 2, 1, 3, 3, 4, 4, 6, 5, 7, 8, 9, 10]
arr = [3, 2, 1, 3, 3, 4, 4, 6, 5, 7, 8, 9, 10, 4, 4, 4, 4, 4]
arr = [3, 2, 1, 3, 3, 4, 4, 6, 5, 7, 8, 9, 10, 4, 4, 4, 4, 49, 99]
# arr = [0, 0, 1, 1, 1]
arr=[0,3,0,3,2]
ans = solve.maxChunksToSorted(arr)
print(ans)
