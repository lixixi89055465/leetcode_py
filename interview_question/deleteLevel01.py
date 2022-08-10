'''


'''


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


from collections import *


class Solution:
    def deleteLevel(self, root, a):
        a=Counter(a)
        q = deque()
        level = 1
        q.append(root)
        rootQ = list()
        if 1 not in a:
            rootQ.append(root)
        qlen = 1
        while q:
            r = q.popleft()
            if level - 1 in a and level not in a:
                rootQ.append(r)
            left = r.left
            right = r.right
            if level + 1 in a:
                r.left = None
                r.right = None
            if left:
                q.append(left)
            if right:
                q.append(right)
            qlen -= 1
            if qlen == 0:
                qlen = len(q)
                level += 1
        return rootQ


solve = Solution()
root = [1, 1, 1, 1, 1, 1, None, 1, 1, None, 1, None, None, None, 1, 1]
r6 = TreeNode(1)
r9 = TreeNode(1)
r10 = TreeNode(1)
r11 = TreeNode(1)
r7 = TreeNode(1, None, r10)
r8 = TreeNode(1, r11, None)
r5 = TreeNode(1, None, r9)
r4 = TreeNode(1, r7, r8)
r2 = TreeNode(1, r4, r5)
r3 = TreeNode(1, r6, None)
r1 = TreeNode(1, r2, r3)
a = [3]
result = solve.deleteLevel(r1, a)
print(result)
