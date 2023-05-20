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
    def mergeKLists(self, lists):
        def mergeTwo(l1, l2):
            ans = ListNode(0, None)
            head = ans
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            if not l1:
                l1 = l2
            while l1:
                head.next = l1
                head = head.next
                l1 = l1.next
            return ans.next

        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return mergeTwo(lists[0], lists[1])
        else:
            return mergeTwo(self.mergeKLists(lists[n // 2:]), self.mergeKLists(lists[:n // 2]))


# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
solve = Solution()
node1 = ListNode(1, ListNode(4, ListNode(5, None)))
node2 = ListNode(1, ListNode(3, ListNode(4, None)))
node3 = ListNode(2, ListNode(6, None))
lists = [node1, node2, node3]
result = solve.mergeKLists(lists)
print(result)
