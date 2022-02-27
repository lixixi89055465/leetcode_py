'''
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]


提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, mem):
        def swap(left, right):
            tmp = mem[left]
            mem[left] = mem[right]
            mem[right] = tmp

        n = (len(mem) - 1) // 2

        def adj(k):
            while k >= 0:
                index = k
                if mem[k * 2] > mem[k]:
                    index = k * 2
                if k * 2 + 1 < len(mem) and mem[k] < mem[k * 2 + 1]:
                    index = k * 2 + 1
                if index != k:
                    swap(k, index)
                k -= 1

        for i in range(n, -1, -1):
            adj(i)
        print(mem)

    def deleteNode(self, ):

        def mergeKLists(self, lists):
            pass


mem = [49, 25, 54, 3, 6, 85, 45, 23, 10]
solve = Solution(mem)
# print(solve.mem)
