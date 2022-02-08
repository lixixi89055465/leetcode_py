'''
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

通过次数604,574提交次数787,365
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        qlen = 1
        ans = 1
        while q:
            p = q.popleft()
            qlen -= 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            if qlen == 0 and q:
                qlen = len(q)
                ans += 1
        return ans


solve = Solution()
root = [3, 9, 20, None, None, 15, 7]
r9 = TreeNode(val=9)
r15 = TreeNode(val=15)
r7 = TreeNode(val=7)
r20 = TreeNode(val=20, left=r15, right=r7)
r3 = TreeNode(val=3, left=r9, right=r20)

result = solve.maxDepth(r3)
print(result)
