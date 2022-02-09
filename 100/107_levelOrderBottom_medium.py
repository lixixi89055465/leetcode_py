'''
107. 二叉树的层序遍历 II
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = [[]]
        qlen = 1
        while q:
            p = q.popleft()
            ans[-1].append(p.val)
            qlen -= 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            if qlen == 0 and q:
                ans.append([])
                qlen = len(q)
        ans.reverse()
        return ans


solve = Solution()
root = [3, 9, 20, None, None, 15, 7]
result = solve.levelOrderBottom(root)
print(result)
