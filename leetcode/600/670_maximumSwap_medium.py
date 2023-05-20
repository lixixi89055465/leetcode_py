'''
maximumSwap
670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]
'''
import heapq


class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        n = num
        i = 0
        while n > 0:
            arr.append((-(n % 10), i))
            n //= 10;
            i += 1
        arr=arr[::-1]
        n=len(arr)
        maxI=-1
        for i in range(n-1):
            maxj=arr[i]
            for j in range(i+1,n):
                if arr[j][0]<maxj[0]:
                    maxj=arr[j]
                    maxI=i
                    break
        print(maxj)
        print(maxI)






solve = Solution()
# num = 2736
# num = 9973
num = 98368
result = solve.maximumSwap(num)
print(result)
