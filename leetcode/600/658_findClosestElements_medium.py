'''
658. 找到 K 个最接近的元素
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b


示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]


提示：

1 <= k <= arr.length
1 <= arr.length <= 104
arr 按 升序 排列
-104 <= arr[i], x <= 104
'''

import math
import collections


class Solution:
    def findClosestElements(self, arr, k, x):
        jinArr = [math.fabs(i - x) for i in arr]
        print(jinArr)
        best = -1
        for i, v in enumerate(jinArr):
            if best == -1 or jinArr[best] > v:
                best = i
        right = best + 1
        left = best - 1
        a = 1
        ans = [arr[best]]
        ans = collections.deque(ans)

        while a < k:
            if left >= 0 and right < len(arr) and jinArr[left] <= jinArr[right]:
                ans.appendleft(arr[left])
                left -= 1
                a += 1
            elif left >= 0 and right < len(arr) and jinArr[left] > jinArr[right]:
                ans.append(arr[right])
                right += 1
                a += 1
            elif left == -1:
                ans.append(arr[right])
                right += 1
                a += 1
            else:
                ans.appendleft(arr[left])
                left -= 1
                a += 1
        return list(ans)


solve = Solution()
# arr = [1, 2, 3, 4, 5]
# k = 4
# x = 3
# arr = [1,2,3,4,5]
# k = 4
# x = -1
arr = [-2, -1, 1, 2, 3, 4, 5]
k = 7
x = 3

result = solve.findClosestElements(arr, k, x)
print(result)
