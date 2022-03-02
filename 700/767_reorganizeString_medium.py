'''
767. 重构字符串
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内
'''

import heapq
import collections


class Solution:
    def reorganizeString(self, s):
        length = len(s)
        counter = collections.Counter(s)
        maxCount = max(counter.items(), key=lambda a: a[1])[1]
        if maxCount > (length + 1) // 2:
            return ''
        queue = [(-x[1], x[0]) for x in counter.items()]
        heapq.heapify(queue)
        ans = list()
        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counter[letter1] -= 1
            counter[letter2] -= 1
            if counter[letter1] > 0:
                heapq.heappush(queue, (-counter[letter1], letter1))
            if counter[letter2] > 0:
                heapq.heappush(queue, (-counter[letter2], letter2))
        if queue:
            ans.append(queue[0][1])
        return ''.join(ans)


solve = Solution()
# s = "aab"
s = "aaab"
result = solve.reorganizeString(s)
print(result)
