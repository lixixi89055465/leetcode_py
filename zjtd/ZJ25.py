# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        hlen = self.getLength(head)

        lastEnd = ListNode()
        lastEnd.next = head
        first = lastEnd
        start = head
        cur = head.next

        for j in range(k, hlen + 1, k):
            start = lastEnd.next
            pre = start
            cur = start.next
            for i in range(1, k):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            if j == k:
                first.next = pre
            start.next = cur
            lastEnd.next=pre
            lastEnd=start

        return first.next

    def getLength(self, head):
        cur = head
        hlen = 0
        while cur:
            hlen += 1
            cur = cur.next
        return hlen


solution = Solution()
n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
k = 2
solution.reverseKGroup(n1, k)
