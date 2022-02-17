'''
515. 在每个树行中找最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。



示例1：



输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
示例2：

输入: root = [1,2,3]
输出: [1,3]


提示：

二叉树的节点个数的范围是 [0,104]
-231 <= Node.val <= 231 - 1

'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        qlen = 1
        ans = []
        ans.append(root.val)
        while q:
            p = q.popleft()
            qlen -= 1
            if qlen == 0:
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                qlen = len(q)
                maxq = float('-inf')
                for i in range(qlen):
                    if maxq < q[i].val:
                        maxq = q[i].val
                if maxq != float('-inf'):
                    ans.append(maxq)
            else:
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return ans


root = [1,2,3]
# root = [1, 3, 2, 5, 3, None, 9]
q = deque(root)
s = deque()
r1 = TreeNode(q.popleft())
s.append(r1)
while s and q:
    a1 = s.popleft()
    while not a1:
        a1 = s.popleft()
    tmp1 = q.popleft()
    if tmp1:
        a1.left = TreeNode(tmp1)
        s.append(a1.left)
    else:
        s.append(None)
    if not q:
        break
    tmp1 = q.popleft()
    if tmp1:
        a1.right = TreeNode(tmp1)
        s.append(a1.right)
    else:
        s.append(None)
solve = Solution()
result = solve.largestValues(r1)
print(result)
